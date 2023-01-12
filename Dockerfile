FROM node:18.12.1-alpine

WORKDIR /projects/all-it

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8080
