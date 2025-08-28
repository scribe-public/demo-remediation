FROM node:latest

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY server.js .
COPY healthcheck.py .

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD curl -f http://localhost:3000/health || exit 1

# Ensure the container does not run processes as root. Use the existing non-root
# `node` user provided by the base image and make the application directory
# owned by that user so runtime files can be written safely.
RUN chown -R node:node /app
USER node

CMD ["sh", "-c", "python healthcheck.py & npm start"] # nosemgrep: dockerfile.security.missing-user.missing-user # fixed added non-root user
