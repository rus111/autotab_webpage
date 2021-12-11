# Environment variables

# project id - replace with your GCP project id
PROJECT_ID=le-wagon-737

# bucket name - replace with your GCP bucket name
BUCKET_NAME="autotab-data"

# choose your region from https://cloud.google.com/storage/docs/locations#available_locations
REGION=europe-west1

set_project:
		@gcloud config set project ${PROJECT_ID}

create_bucket:
		@gsutil mb -l ${REGION} -p ${PROJECT_ID} gs://${BUCKET_NAME}

# path to the file to upload to GCP (the path to the file should be absolute or should match the directory where the make command is ran)
# replace with your local path to the `train_1k.csv` and make sure to put the path between quotes
LOCAL_PATH="/home/ruslan/code/rus111/autotab_webpage/requirements.txt"
			


# bucket directory in which to store the uploaded file (`data` is an arbitrary name that we choose to use)
BUCKET_FOLDER=data

# name for the uploaded file inside of the bucket (we choose not to rename the file that we upload)
#BUCKET_FILE_NAME=$(shell basename ${LOCAL_PATH})
BUCKET_FILE_NAME=.

##### Machine configuration - - - - - - - - - - - - - - - -

REGION=europe-west1

PYTHON_VERSION=3.7
FRAMEWORK=TensorFlow
RUNTIME_VERSION=2.6

##### Package params  - - - - - - - - - - - - - - - - - - -

PACKAGE_NAME=autotab
FILENAME=wave-file

##### Job - - - - - - - - - - - - - - - - - - - - - - - - -

JOB_NAME=audio_job$(shell date +'%Y%m%d_%H%M%S')


run_locally:
	@python -m ${PACKAGE_NAME}.${FILENAME}

gcp_submit_training:
	gcloud ai-platform jobs submit training ${JOB_NAME} \
		--job-dir gs://${BUCKET_NAME}/${BUCKET_TRAINING_FOLDER} \
		--package-path ${PACKAGE_NAME} \
		--module-name ${PACKAGE_NAME}.${FILENAME} \
		--python-version=${PYTHON_VERSION} \
		--runtime-version=${RUNTIME_VERSION} \
		--region ${REGION} \
		--stream-logs

# upload_data:
#     # @gsutil cp train_1k.csv gs://wagon-ml-my-bucket-name/data/train_1k.csv
# 		# @gsutil -m cp -r ${LOCAL_PATH} gs://${BUCKET_NAME}/${BUCKET_FOLDER}/${BUCKET_FILE_NAME}
# 		@gsutil -m cp -r ${LOCAL_PATH} gs://${BUCKET_NAME}

upload_data:
    # @gsutil cp train_1k.csv gs://wagon-ml-my-bucket-name/data/train_1k.csv
	@gsutil cp ${LOCAL_PATH} gs://${BUCKET_NAME}
# ----------------------------------
#         LOCAL SET UP
# ----------------------------------

install_requirements:
	@pip install -r requirements.txt

# ----------------------------------
#         HEROKU COMMANDS
# ----------------------------------

streamlit:
	-@streamlit run streamlit_app/autotab-app.py

heroku_login:
	-@heroku login

heroku_create_app:
	-@heroku create ${APP_NAME}

deploy_heroku:
	-@git push heroku master
	-@heroku ps:scale web=1

# ----------------------------------
#    LOCAL INSTALL COMMANDS
# ----------------------------------
install:
	@pip install . -U

clean:
	@rm -fr */__pycache__
	@rm -fr __init__.py
	@rm -fr build
	@rm -fr dist
	@rm -fr *.dist-info
	@rm -fr *.egg-info
	-@rm model.joblib

