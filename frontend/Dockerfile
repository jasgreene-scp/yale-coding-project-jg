FROM node:18

WORKDIR /frontend/app

COPY ./app /frontend/app

COPY package*.json ./
RUN npm install

EXPOSE 5173

CMD ["npm", "run", "dev"]
