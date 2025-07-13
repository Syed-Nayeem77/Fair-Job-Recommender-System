# IAM key for SSH access
variable "key_name" {
  description = "EC2 key pair name for SSH access"
  type        = string
}

# Optional variable to control instance type
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}
