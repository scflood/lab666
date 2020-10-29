
|  Method 	| Local  	| Same-Zone  	|  SameReg/Diff Zone 	| Europe |
|---------- |---------- |-------------- |-----------------------|--------|
|   REST add	|   .0038	|   0.0025 	| 0.0029 	| 0.028
|   gRPC add	|  0.0004 	|  0.0005 	|  0.0007  	|0.169
|   REST img	|  0.005 	|   0.006	|0.0088   	|1.185
|   gRPC img	|  0.007     | 0.011  	| 0.011  	|0.194
|   PING        |    4.9e-5   | 0.000325     |  0.000467     |0.138491

You should measure the basic latency  using the `ping` command - this can be construed to be the latency without any RPC or python overhead.

You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC. You should explicitly comment on the role that network latency plays -- it's useful to know that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries.