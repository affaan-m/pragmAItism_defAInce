'use client'

import React, { useState } from 'react'
import { GlitchText } from './glitch-text'

export const TweetGenerator: React.FC = () => {
  const [generatedTweet, setGeneratedTweet] = useState('')
  const [isGenerating, setIsGenerating] = useState(false)

  const generateTweet = async () => {
    setIsGenerating(true)
    try {
      const response = await fetch('http://localhost:8000/api/generate-tweet', {
        method: 'POST'
      })
      const data = await response.json()
      setGeneratedTweet(data.tweet)
    } catch (error) {
      console.error('Error:', error)
    }
    setIsGenerating(false)
  }

  const postTweet = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/post-tweet', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ tweet: generatedTweet })
      })
      const data = await response.json()
      if (data.success) {
        alert('Tweet posted successfully!')
      }
    } catch (error) {
      console.error('Error:', error)
    }
  }

  return (
    <div className="space-y-4">
      <GlitchText text="Tweet Generator" className="text-xl font-mono" />
      
      <div className="p-4 bg-accent/10 rounded-lg backdrop-blur-sm">
        <button
          onClick={generateTweet}
          disabled={isGenerating}
          className="px-4 py-2 bg-accent/20 rounded hover:bg-accent/30 transition-colors"
        >
          {isGenerating ? 'Generating...' : 'Generate Tweet'}
        </button>

        {generatedTweet && (
          <div className="mt-4">
            <p className="font-mono text-green-400">{generatedTweet}</p>
            <button
              onClick={postTweet}
              className="mt-2 px-4 py-2 bg-accent/20 rounded hover:bg-accent/30 transition-colors"
            >
              Post Tweet
            </button>
          </div>
        )}
      </div>
    </div>
  )
} 