* In-Process...

# In-Process Triton Server API[#](#in-process-triton-server-api "Link to this heading")

The Triton Inference Server provides a backwards-compatible C API/ python-bindings/java-bindings that
allows Triton to be linked directly into a C/C++/java/python application. This API
is called the âTriton Server APIâ or just âServer APIâ for short. The
API is implemented in the Triton shared library which is built from
source contained in the [core
repository](https://github.com/triton-inference-server/core). On Linux
this library is libtritonserver.so and on Windows it is
tritonserver.dll. In the Triton Docker image the shared library is
found in /opt/tritonserver/lib. The header file that defines and
documents the Server API is
[tritonserver.h](https://github.com/triton-inference-server/core/blob/main/include/triton/core/tritonserver.h).
[Java bindings for In-Process Triton Server API](../customization_guide/inprocess_java_api.md#java-bindings-for-in-process-triton-server-api)
are built on top of tritonserver.h and can be used for Java applications that
need to use Tritonserver in-process.

All capabilities of Triton server are encapsulated in the shared
library and are exposed via the Server API. The tritonserver
executable implements HTTP/REST and GRPC endpoints and uses the Server
API to communicate with core Triton logic. The primary source files
for the endpoints are [grpc\_server.cc](https://github.com/triton-inference-server/server/blob/main/src/grpc/grpc_server.cc) and
[http\_server.cc](https://github.com/triton-inference-server/server/blob/main/src/http_server.cc). In these source files you can
see the Server API being used.

You can use the Server API in your own application as well. A simple
example using the Server API can be found in
[simple.cc](https://github.com/triton-inference-server/server/blob/main/src/simple.cc).