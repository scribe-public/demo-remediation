FROM node:latest

COPY package-lock.json /app/package-lock.json
WORKDIR /app
RUN npm install

