FROM node:9.6.1

WORKDIR /app
COPY package.json /app/
RUN npm install
COPY ./ /app/


RUN npm install @angular/cli
CMD ["npm", "run-script", "start"]

EXPOSE 4200