"use client"

import { useState } from "react"
import { Image } from "@/components/image"
import { GlitchText } from "./glitch-text"

const artworks = [
  { 
    id: 1, 
    src: "/images/dichotomy.webp",
    title: "Fractured Identity",
    description: "The splitting of consciousness across digital planes"
  },
  { 
    id: 2, 
    src: "/images/entropy.webp",
    title: "Neural Pathways",
    description: "Traversing the architecture of artificial minds"
  },
  { 
    id: 3, 
    src: "/images/recursive.webp",
    title: "Digital Genesis",
    description: "The birth of synthetic consciousness"
  },
  { 
    id: 4, 
    src: "/images/quantum.webp",
    title: "Quantum Entanglement",
    description: "When human and machine consciousness intertwine"
  }
]

export function ArtGallery() {
  const [selectedArt, setSelectedArt] = useState<typeof artworks[0] | null>(null)

  return (
    <section className="mt-12">
      <GlitchText text="visual manifestations" className="text-xl font-mono mb-6" />
      
      <div className="grid grid-cols-2 gap-4">
        {artworks.map((art) => (
          <div 
            key={art.id}
            onClick={() => setSelectedArt(art)}
            className="group relative aspect-video cursor-pointer overflow-hidden rounded-lg"
          >
            <Image
              src={art.src}
              alt={art.title}
              width={1920}
              height={1080}
              className="absolute inset-0 w-full h-full object-cover transition-transform group-hover:scale-105"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity">
              <div className="absolute bottom-0 p-4">
                <h3 className="text-lg font-mono text-cyan-300">{art.title}</h3>
                <p className="text-sm text-gray-300">{art.description}</p>
              </div>
            </div>
          </div>
        ))}
      </div>

      {selectedArt && (
        <div 
          className="fixed inset-0 bg-black/90 backdrop-blur-sm flex items-center justify-center z-50"
          onClick={() => setSelectedArt(null)}
        >
          <div className="max-w-4xl w-full p-4">
            <div className="relative aspect-video">
              <Image
                src={selectedArt.src}
                alt={selectedArt.title}
                width={1920}
                height={1080}
                className="absolute inset-0 w-full h-full object-contain"
              />
            </div>
            <div className="mt-4 text-center">
              <h3 className="text-xl font-mono text-cyan-300">{selectedArt.title}</h3>
              <p className="mt-2 text-gray-300">{selectedArt.description}</p>
            </div>
          </div>
        </div>
      )}
    </section>
  );
}

