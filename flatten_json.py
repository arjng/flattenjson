import json
import sys

# Take json string as input, and return the flattened json string.
def flatten_input(json_string):
	try:
		obj = json.loads(json_string)
	except json.decoder.JSONDecodeError as err:
		print("Incorrect JSON format: {0}".format(err))
		raise
	except BaseException as err:
		print("Unexpected error: {0}".format(err))
		raise
	result = json.dumps(flatten(obj))
	return result

# Given a dict, return the flattened dict.
def flatten(obj):
	result = {}

	def flatten_recurse(obj, prefix = ""):
		for key in obj:
			result_key = prefix + "." + key if prefix else key
			if isinstance(obj[key], dict):
				flatten_recurse(obj[key], result_key)
			else:
				result[result_key] = obj[key]
	flatten_recurse(obj)
	return result

if __name__ == '__main__':	
	data = ''.join(sys.stdin.readlines())
	print(flatten_input(data))


