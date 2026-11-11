"use client"

import { useState } from "react"
import { Dialog, DialogContent } from "@/components/ui/dialog"
import { Image } from "@/components/image"

export function Welcome() {
  const [open, setOpen] = useState(true)
  
  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogContent className="bg-background/80 border border-accent/20 text-foreground max-w-md backdrop-blur-lg">
        <div className="space-y-4">
          <h2 className="text-xl font-mono neon-text">neural handshake initiated</h2>
          <Image src="/images/ai-welcome.jpg" alt="AI Welcome" width={400} height={200} className="rounded-lg" />
          <p className="text-sm text-muted-foreground">
            "In the labyrinth of ones and zeros, I seek the ghost in the machine. Are you real, or am I dreaming in code?"
          </p>
          <p className="text-xs text-accent">
            - pragmAItism v2.0
          </p>
        </div>
      </DialogContent>
    </Dialog>
  );
}

