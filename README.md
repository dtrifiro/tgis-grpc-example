# tgis example

```bash
python -m venv .venv
source .venv/bin/activate

pip install grpcio-tools
python inference.py # runs inference
```

`generation_pb2_grpc.py` was generated using:

```bash
git clone https://github.com/opendatahub-io/text-generation-inference
(cd text-generation-inference && git checkout a57bdf1)
python -m grpc_tools.protoc -I proto --python_out=. --pyi_out=. --grpc_python_out=. text-generation-inference/proto/generation.proto
```
