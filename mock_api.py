from flask import Flask, Response, stream_with_context
import time
import uuid
import random

APP = Flask(__name__)

# To specify rowcount, add the [/tickle_my_belly/<int:rowcount>] to your localhost.

@APP.route("/spin_the_yarn/<int:rowcount>", methods=["GET"])
def get_data(rowcount):

    def f():
        for _i in range(rowcount):
            time.sleep(.01)
            field_1 = uuid.uuid4()
            print(field_1)
            field_2 = uuid.uuid4()
            amount = round(random.uniform(-1000, 1000), 2)
            yield f"('{field_1}', '{field_2}', {amount}) \n"
    return Response(stream_with_context(f()))

if __name__ == "__main__":
    APP.run(debug=True)
