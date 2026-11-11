"use client"

import { useEffect, useState } from "react"
import { cn } from "@/lib/utils"

interface GlitchTextProps {
  text: string
  className?: string
}

export function GlitchText({ text, className }: GlitchTextProps) {
  const [isGlitching, setIsGlitching] = useState(false)

  useEffect(() => {
    const interval = setInterval(() => {
      setIsGlitching(true)
      setTimeout(() => setIsGlitching(false), 50)
    }, 5000)

    return () => clearInterval(interval)
  }, [])

  return (
    <div 
      className={cn(
        "relative inline-block",
        isGlitching && "animate-glitch",
        className
      )}
      data-text={text}
    >
      {text}
    </div>
  )
}

