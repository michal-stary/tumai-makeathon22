import json
import logging
import sys
from http import HTTPStatus
import argparse

from flask import Flask, request, Response, render_template
from flask_cors import CORS, cross_origin
from werkzeug.exceptions import HTTPException

from reg_score.scorer import Scorer

logger = logging.getLogger('main')



class Server(object):
    app = None
    def __init__(self, port, host, scorer, proxy_url_prefix='/'):
        self.proxy_url_prefix = proxy_url_prefix

        self.app = Flask(__name__, static_folder='./static/')
        self.app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
        cors = CORS(self.app)

        self.app.add_url_rule(rule='/score', view_func=self.score, methods=['POST'])

        self.app.register_error_handler(HTTPStatus.INTERNAL_SERVER_ERROR, self.internal_server_error)
        self.app.register_error_handler(HTTPException, self._handle_http_exception)

        self.scorer = scorer
        self.port = port
        self.host = host

    def score(self):
        try:
            json_file = request.get_json()
            text = json_file["text"]
            print(text)

            # model = json_file["model"] if "model" in json_file else "combined"

            result = self.scorer(text=text)

            response = Response(response=json.dumps({'result': result}))
            response.content_type = 'application/json'
            return response  # return Response(status=HTTPStatus.BAD_REQUEST)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
            return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)

    # def demo(self):
    #     contract_render_url = posixpath.join(self.proxy_url_prefix, 'file')
    #     return render_template('index.html', contract_render_url=contract_render_url)
    #
    # def visualisation(self):
    #     return render_template('visualisation.html')

    def run(self):
        self.app.run(host=self.host, port=self.port, debug=False)

    def internal_server_error(self, error):
        return self._not_ok(str(error), HTTPStatus.INTERNAL_SERVER_ERROR)

    def _handle_http_exception(self, error: HTTPException):
        return self._not_ok(str(error), error.code)

    def _not_ok(self, error, status):
        return self.app.response_class(response=json.dumps({"message": error}), status=status,
                                       mimetype='application/json')

def main():
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('opt_pos_arg', type=int, nargs='?',
                        help='An optional integer positional argument')
    args = parser.parse_args()
    PORT = args.opt_pos_arg if args.opt_pos_arg is not None else 8080

    scorer = Scorer()

    logger.info(f"Starting server on port {PORT}")
    Server(port=PORT, host="0.0.0.0", scorer=scorer).run()

if __name__ == "__main__":
    sys.exit(main())