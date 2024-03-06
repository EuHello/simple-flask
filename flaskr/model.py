from flask import Flask, request, jsonify, Blueprint

app = Flask(__name__)

# bp = Blueprint('model', __name__)
bp = Blueprint('model', __name__, url_prefix='/model')


def model_inference(input_data):
    # Placeholder functions
    result = {"prediction": "1"}
    return result


# a simple page that says hello
@bp.route('/view')
def hello_index():
    return 'Viewing model!'


@bp.route('/predict', methods=['POST'])
def predict():
    # get input data from request
    input_data = request.json

    # Perform model inference
    prediction = model_inference(input_data)

    # Return prediction result as JSON
    return jsonify(prediction)
