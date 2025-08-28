FROM node:latest

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY server.js .
COPY healthcheck.py .

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD curl -f http://localhost:3000/health || exit 1

RUN chown -R node:node /app
USER node

CMD ["sh", "-c", "python healthcheck.py & npm start"] # nosemgrep: dockerfile.security.missing-user.missing-user # fixed added non-root USER
