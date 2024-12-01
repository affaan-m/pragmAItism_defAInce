'use client';

import { GlitchText } from "@/components/glitch-text"
import { TokenStats } from "@/components/token-stats"
import { Analytics } from "@/components/analytics"

export default function AmIAFake() {
  return (
    <div className="p-6">
      <GlitchText text="am i a fake?" className="text-2xl font-mono mb-6" />
      <div className="space-y-8">
        <TokenStats />
        <Analytics />
      </div>
    </div>
  )
} 