import bucket_pb2_grpc  # as service
import bucket_pb2  # as message
import grpc
from db_config import conn
from concurrent import futures
import user_service_client


class BucketService(bucket_pb2_grpc.BucketServicer):
    def GetInformation(self, request, context):
        bucket_id = request.bucket_id
        cursor = conn.cursor()
        query = 'SELECT id, name, owner_id FROM bucket where id = %s'
        cursor.execute(query % bucket_id)
        for row in cursor:
            print(row)
            user_service = user_service_client.UserClient()
            user_info = user_service.get_user_by_id(user_id=row['owner_id'])
            print (user_info)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bucket_pb2_grpc.add_BucketServicer_to_server(servicer=BucketService(), server=server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    print('Bucket Server is staring...')
    serve()
