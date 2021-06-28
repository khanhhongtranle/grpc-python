import bucket_pb2_grpc
import bucket_pb2
import grpc


class BucketClient:
    def __init__(self):
        self.host = 'localhost'
        self.port = 50051
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.port))
        self.stub = bucket_pb2_grpc.BucketStub(channel=self.channel)

    def get_bucket_information(self, bucket_id):
        request = bucket_pb2.InformationRequest(bucket_id=bucket_id)
        return self.stub.GetInformation(request)


if __name__ == '__main__':
    client = BucketClient()
    response = client.get_bucket_information("2")
    print(response)

