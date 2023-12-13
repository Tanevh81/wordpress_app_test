# Stage 1: Prepare the base operating system image
FROM ubuntu:20.04 AS base

# Update the package list and install necessary dependencies
RUN apt-get update && \
    apt-get install -y \
    # Add your required dependencies here
    && rm -rf /var/lib/apt/lists/*

# Stage 2: Install and configure WordPress
FROM wordpress:php7.4-apache AS wordpress

# Add any additional configurations or WordPress setup commands here
