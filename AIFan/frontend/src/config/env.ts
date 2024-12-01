export const env = {
  NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000',
  NEXT_PUBLIC_TWITTER_CALLBACK: process.env.NEXT_PUBLIC_TWITTER_CALLBACK || 'http://localhost:3000/api/auth/twitter/callback'
} 