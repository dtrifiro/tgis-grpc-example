import re
from inference import GrpcClient

model_id = "flan-t5-small"
grpc_port = 433
infer_endpoint = "https://localhost/"

hostname = re.sub("https://|http://", "", infer_endpoint)
if hostname[-1] == "/":
    hostname = hostname[:-1]

print(f"Querying host {hostname} with grpc port {grpc_port}")

client = GrpcClient(
    hostname,
    443,
    verify=False,
)

# BATCH REQUEST EXAMPLE
resps = client.make_request(
    [
        "At what temperature does Nitrogen boil?",
        "How many days are in a week?",
        "How far away from Earth is Jupiter?"
    ],
    model_id=model_id
)
print([resp.text for resp in resps.responses])

# STREAM EXAMPLE
resp_stream = client.make_request_stream("At what temperature does Nitrogen boil?", model_id=model_id)
for resp in resp_stream:
    if resp.tokens:
        print("GENERATED TOKEN: ", resp.tokens[0].text)
        print("CLEANED TEXT OUT:", resp.text)
    print(resp)
