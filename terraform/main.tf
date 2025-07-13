provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "job_rec_instance" {
  ami           = "ami-0c55b159cbfafe1f0" # Ubuntu 22.04 (update as needed)
  instance_type = "t2.micro"
  key_name      = var.key_name
  tags = {
    Name = "job-recommender"
  }
}
