# Mô tả đề bài

Có 2 services là Bucket và User độc lập nhau.

Bucket service dùng để thực hiện các thao tác liên quan đến buckets. 

Bucket service sử dụng database là MySQL.

User service dùng để thực hiện các thao thác về users.

User service sử dụng database là MongoDB.

Tạo một kết nối gRPC để 2 services trên có thể giao tiếp truyền nhận thông tin với nhau.

### Ví dụ yêu cầu cụ thể: 
Cần trả về thông tin của một bucket như sau: id_bucket, name_bucket, user_name

### Mô tả DB:
TABLE USERS(
    id PK,
    name
)

TABLE BUCKETS(
    id PK,
    name,
    owner_id
)

### Run bucket service:
`cd ./microservices_example/bucket-service/ `
`python server.py`

### Run bucket client:
`cd ./microservices_example/bucket-service/ `
`python client.py`