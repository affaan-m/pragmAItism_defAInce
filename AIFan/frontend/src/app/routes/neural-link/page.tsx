'use client';

import { GlitchText } from "@/components/glitch-text"
import { Settings } from "@/components/settings"

export default function NeuralLink() {
  return (
    <div className="p-6">
      <GlitchText text="neural link" className="text-2xl font-mono mb-6" />
      <Settings />
    </div>
  )
} 