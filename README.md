# Protobuf for Rena 2 SDK

## Generate gRPC code

Code for Python is generated automatically by the CI. You just need to `git pull` to get the generated code after any pushed changes to the .proto. If you still need to generate these files locally, you can do the following commands

### For Python:

Just install `pip install mypy-protobuf` to generate the mypy stubs, and run:

```python
python -m grpc_tools.protoc -I./protos --python_out=./python/rena2_sdk_api --grpc_python_out=./python/rena2_sdk_api --mypy_out=./python/rena2_sdk_api --mypy_grpc_out=./python/rena2_sdk_api  ./protos/*.proto
```
