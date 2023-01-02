FROM node:18.12.1-alpine

WORKDIR /project

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8080
