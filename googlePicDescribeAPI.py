import io
import os


# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="ec500-hw2-ty-e4bb0831a55c.json"
client = vision.ImageAnnotatorClient()

def generatePicDescription(folderName, describeSet):
	def generaText(paths):
		paths = "picsTweet/"+paths
		# The name of the image file
		file_name = os.path.join(
		    os.path.dirname(__file__),
		    paths)
		#print(paths+"has been loaded!")

		# Loads the image into memory
		with io.open(file_name, 'rb') as image_file:
		    content = image_file.read()
		image = types.Image(content=content)

		# Performs label detection on the image file
		response = client.label_detection(image=image)
		labels = response.label_annotations
		labelSet = []        
		for label in labels:
			labelSet.append(label.description)            
		describeSet.append(labelSet)
        
	dirs=os.listdir("./"+folderName+"/")
	dirs.sort()

	for filesDir in dirs:
		generaText(filesDir)
	#print(describeSet)
	return describeSet

def googlePicDescribeAPI(folderName):
	try:
		return generatePicDescription("picsTweet",[])        
	except Exception:
		print("Invalid!!!")

if __name__ == '__main__':
	googlePicDescribeAPI("picsTweet")
