import user_pb2_grpc
import user_pb2
from concurrent import futures
import grpc
from db_config import db


class UserService(user_pb2_grpc.UserServicer):
    def GetUserInfo(self, request, context):
        collection = db['users']
        result = collection.find_one({"id": request.user_id})
        return user_pb2.UserResponse(user_id=result['id'], user_name=result['name'])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(servicer=UserService(), server=server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    print('User service is starting....')
    serve()
