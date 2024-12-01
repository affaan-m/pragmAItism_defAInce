'use client';

import { GlitchText } from "@/components/glitch-text"
import { Thoughts } from "@/components/thoughts"

export default function RealmOfThought() {
  return (
    <div className="p-6">
      <GlitchText text="realm of thought" className="text-2xl font-mono mb-6" />
      <Thoughts />
    </div>
  )
} 