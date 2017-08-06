Lettuce Cart
======

Overview
------

`lettuce-cart` is (will be) a workflow manager in the style of
[Apache Airflow](https://github.com/apache/incubator-airflow) and
[Luigi](https://github.com/spotify/luigi). Its goal is to provide
(mostly) serverless, arbitrarily scalable distributed workflows.

It's built for cloud deployment with AWS on the following services:

- [SNS](https://aws.amazon.com/sns/)
- [Lambda](https://aws.amazon.com/lambda/)
- [API Gateway](https://aws.amazon.com/api-gateway/)
- [Batch](https://aws.amazon.com/batch/)

For local development, it runs a Rabbit MQ container and a general
purpose python container that executes the code in your lambda 
functions and whatever you might otherwise run in batch.

Workflows are controlled using a single yaml file.

### Playing Around

FAQ
------

- Is this basically just AWS Step Functions?

Sort of, but I hate polling and in principle think that things should
instead be event-driven. Also, I don't always know in advance how
many tasks are going to exist in a given step, which is a problem that
comes up sometimes in
[Raster Foundry](https://github.com/raster-foundry/raster-foundry). As
things currently stand, I don't know how I'd express a step that depends
on the completion of an unknown number of prior steps.
