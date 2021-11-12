from diagrams import Diagram
from diagrams.onprem.database import  MongoDB
from diagrams.onprem.container import Docker

with Diagram("Remainders microservices"):
    atlas = MongoDB("Atlas DBaaS")
    remainders_backend = Docker("Remainders backend")
    remainders_frontend = Docker("Remainders frontend")
    remainders_register_backend = Docker("Registeration backend")
    remainders_register_frontend = Docker("Registration frontend")

    atlas >> remainders_backend >> remainders_frontend
    atlas >> remainders_register_backend >> remainders_register_frontend
    remainders_register_frontend >> remainders_register_backend 