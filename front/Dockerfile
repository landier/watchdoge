# Stage 1 - build environment
FROM node:latest as build
LABEL maintainer="nicolas.landier@gmail.com"

WORKDIR /usr/src/front
COPY package*.json yarn.lock ./
RUN yarn

COPY . ./

RUN yarn build

# Stage 2 - production environment
FROM nginx:alpine
LABEL maintainer="nicolas.landier@gmail.com"

COPY --from=build /usr/src/front/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
