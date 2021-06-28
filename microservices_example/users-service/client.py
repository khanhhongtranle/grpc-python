import grpc
import user_pb2_grpc
import user_pb2


class UserClient:
    def __init__(self):
        self.host = 'localhost'
        self.port = 50052
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.port))
        self.stub = user_pb2_grpc.UserStub(channel=self.channel)

    def get_user_by_id(self, user_id):
        request = user_pb2.UserRequest(user_id=user_id)
        return self.stub.GetUserInfo(request)


if __name__ == '__main__':
    client = UserClient()
    response = client.get_user_by_id("0")
