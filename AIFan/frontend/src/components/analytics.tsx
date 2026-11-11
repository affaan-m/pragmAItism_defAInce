import React from 'react'
import { GlitchText } from './glitch-text'

export const Analytics: React.FC = () => {
  return (
    <div className="mt-8 p-4 border border-accent/20 rounded-lg backdrop-blur-sm">
      <GlitchText text="Analytics" className="text-xl font-mono mb-4" />
      <div className="space-y-2">
        <p className="text-sm text-accent">Total Users: 0</p>
        <p className="text-sm text-accent">Active Users: 0</p>
        <p className="text-sm text-accent">Tweets Generated: 0</p>
      </div>
    </div>
  )
}

