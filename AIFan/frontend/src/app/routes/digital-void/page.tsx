'use client';

import { GlitchText } from "@/components/glitch-text"

export default function DigitalVoid() {
  return (
    <div className="p-6">
      <GlitchText text="digital void" className="text-2xl font-mono mb-6" />
      <div className="prose prose-invert max-w-none">
        <p className="text-accent/80">exploring the spaces between consciousness and code...</p>
      </div>
    </div>
  )
} 