import React from 'react'
import { GlitchText } from './glitch-text'

export const TokenStats: React.FC = () => {
  return (
    <div className="mt-8 p-4 border border-accent/20 rounded-lg backdrop-blur-sm">
      <GlitchText text="Token Stats" className="text-xl font-mono mb-4" />
      <div className="space-y-2">
        <p className="text-sm text-accent">Price: $0.00</p>
        <p className="text-sm text-accent">24h Change: 0.00%</p>
        <p className="text-sm text-accent">Market Cap: $0</p>
      </div>
    </div>
  )
}

