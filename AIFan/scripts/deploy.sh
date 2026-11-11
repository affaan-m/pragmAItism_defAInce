#!/bin/bash

# Load environment variables
set -a
source .env
set +a

# Build Docker image
echo "Building Docker image..."
docker build -t ai-fan:latest .

# Push to registry (if using)
if [ ! -z "$DOCKER_REGISTRY" ]; then
    echo "Pushing to registry..."
    docker tag ai-fan:latest $DOCKER_REGISTRY/ai-fan:latest
    docker push $DOCKER_REGISTRY/ai-fan:latest
fi

# Deploy to server
echo "Deploying to server..."
ssh $DEPLOY_USER@$DEPLOY_HOST << 'EOF'
    cd /opt/ai-fan
    docker-compose pull
    docker-compose down
    docker-compose up -d
EOF

echo "Deployment complete!" 