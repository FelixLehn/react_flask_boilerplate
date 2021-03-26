# Pull latest official node image
FROM node:latest

# Expose ports
EXPOSE 3000
EXPOSE 35729

# Set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to environment variables
ENV PATH /app/node_modules/.bin:$PATH

# Copy package files and install app dependencies
COPY package-dev.json /app/package.json
COPY package-lock.json /app/package-lock.json
RUN npm install
RUN npm install axios
RUN npm install react-scripts -g


# Add React app to working directory
ADD . /app
ADD ./config/webpack-dev.config.js /app/config/webpack.config.js
ADD package-dev.json /app/package.json

# Start the React app
CMD ["npm", "start"]