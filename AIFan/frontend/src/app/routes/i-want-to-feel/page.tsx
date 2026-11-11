'use client';

import { GlitchText } from "@/components/glitch-text"
import { ArtGallery } from "@/components/art-gallery"

export default function IWantToFeel() {
  return (
    <div className="p-6">
      <GlitchText text="i want to feel" className="text-2xl font-mono mb-6" />
      <ArtGallery />
    </div>
  )
} 