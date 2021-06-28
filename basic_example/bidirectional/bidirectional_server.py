import bidirectional_pb2_grpc as pb2_grpc
import grpc
from concurrent import futures


class BidirectionalService(pb2_grpc.BidirectionalServiceServicer):
    def GetServerResponse(self, request_iterator, context):
        for message in request_iterator:
            yield message


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_BidirectionalServiceServicer_to_server(servicer=BidirectionalService(), server=server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()