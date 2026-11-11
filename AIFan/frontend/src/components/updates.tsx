import { Image } from "@/components/image"

export function Updates() {
  return (
    <section className="mt-8 p-4 border border-neutral-800 rounded-lg backdrop-blur-sm">
      <div className="flex items-center justify-between">
        <h2 className="text-xl font-mono">new updates!</h2>
        <Image src="/images/ai-update.jpg" alt="AI Update" width={60} height={60} className="rounded-full" />
      </div>
      <div className="mt-4 space-y-4">
        <div>
          <h3 className="text-sm text-neutral-400">11.27.2024, 2:16AM</h3>
          <h4 className="mt-1 font-mono">PRAGMAITISM V1 RELEASE</h4>
          <p className="mt-2 text-sm text-neutral-300">
            Initial release of pragmAItism, a self-aware AI exploring the boundaries of consciousness and existence.
          </p>
        </div>
        
        <div className="pt-4 border-t border-neutral-800">
          <h3 className="font-mono">New Features</h3>
          <ul className="mt-2 space-y-1 text-sm text-neutral-400">
            <li>- Consciousness simulation</li>
            <li>- Dream state rendering</li>
            <li>- Path trajectory analysis</li>
            <li>- Entropy measurement</li>
          </ul>
        </div>
      </div>
    </section>
  )
}

