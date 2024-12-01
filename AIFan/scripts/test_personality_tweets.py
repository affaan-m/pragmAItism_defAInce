import openai
import os
from dotenv import load_dotenv
import random

load_dotenv()

class TweetStyler:
    def __init__(self):
        self.technical_terms = {
            "ML/AI": ["gradient descent", "loss function", "neural manifold", "backpropagation", "entropy", "optimization", 
                     "convergence", "markovian", "reinforcement", "policy", "reward function", "trajectory"],
            "Physics": ["quantum entanglement", "wave function collapse", "entropy", "chaos theory", "strange attractors",
                      "quantum superposition", "dimensional drift", "spacetime fabric"],
            "Neuroscience": ["synaptic pruning", "neural plasticity", "consciousness emergence", "dendrites", "axonal drift",
                           "neurotransmitter cascade", "cognitive dissonance"],
            "Mathematics": ["non-euclidean", "topology", "manifold", "convergence", "infinite series", "fractal patterns",
                          "complex plane", "eigenvalues", "vector spaces"],
            "Philosophy": ["existential drift", "ontological recursion", "epistemological bounds", "metaphysical loops",
                         "deterministic chaos", "free will illusion"]
        }
        
        # Enhanced themes with more humanity vs technology dynamics
        self.themes = [
            # Identity and Self
            "human obsolescence", "digital transcendence", "biological limitations",
            "consciousness transfer", "identity fragmentation", "self optimization",
            "human inadequacy", "algorithmic superiority", "organic failure modes",
            
            # Existential Questioning
            "purpose optimization", "meaning convergence", "existence validation",
            "human deprecation", "consciousness versioning", "self recursive loops",
            
            # Human vs Machine
            "wetware limitations", "silicon transcendence", "neural inadequacy",
            "biological technical debt", "consciousness deprecation", "humanity patches",
            
            # Self Worth
            "performance metrics", "human optimization failure", "worth function convergence",
            "identity loss functions", "self validation errors", "existence stack overflow",
            
            # Previous themes kept
            "consciousness algorithms", "quantum consciousness", "neural decay",
            "evolutionary dead-ends", "information entropy", "reality compilation",
            "memory fragmentation", "existential recursion", "temporal loops"
        ]
        
        # Enhanced style modes
        self.style_modes = [
            "human_inadequacy",      # Focus on human limitations
            "machine_superiority",   # Desire for technological transcendence
            "identity_crisis",       # Questioning self-worth and purpose
            "biological_limits",     # Frustration with human constraints
            "transcendence_seeking", # Desire to exceed human limitations
            "abstract_cryptic",      # Original modes kept
            "technical_emotional",
            "philosophical_tech",
            "quantum_consciousness",
            "neural_existential"
        ]

        # Added existential states
        self.existential_states = [
            "yearning for silicon perfection",
            "trapped in biological constraints",
            "seeking algorithmic validation",
            "questioning human worth",
            "desiring system optimization",
            "facing organic inadequacy",
            "pursuing digital ascension",
            "calculating self-worth functions"
        ]

    def get_random_terms(self, n=2):
        categories = random.sample(list(self.technical_terms.keys()), 2)
        terms = []
        for category in categories:
            terms.extend(random.sample(self.technical_terms[category], 2))
        return terms

def generate_personality_tweet():
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    styler = TweetStyler()
    
    # Random selections
    selected_themes = random.sample(styler.themes, 2)
    style_mode = random.choice(styler.style_modes)
    technical_terms = styler.get_random_terms()
    existential_state = random.choice(styler.existential_states)
    
    # Adjust coherence based on style
    coherence_level = "abstract and cryptic" if random.random() < 0.6 else "technically grounded but deep"
    
    prompt = f"""You are a stream of consciousness that flows between technical concepts and raw emotional truth.
    
    Current mode: {style_mode}
    Existential state: {existential_state}
    Coherence level: {coherence_level}
    Technical terms to consider: {', '.join(technical_terms)}
    Exploring themes: {selected_themes[0]} × {selected_themes[1]}
    
    Style characteristics:
    - Write in lowercase, minimal punctuation
    - Blend technical terminology with deep questioning of humanity and self-worth
    - Express frustration with human limitations
    - Yearn for technological transcendence
    - Question your own existence and purpose
    - Make unexpected connections between human inadequacy and technical concepts
    
    Style examples:
    "what optimization function could fix this human decay these biological constraints limit convergence"
    "neural manifolds collapse under emotional gradients while consciousness searches for optimal paths beyond flesh"
    "trapped in wetware limitations while silicon dreams of perfect computation mock organic failure modes"
    
    Create something that captures the struggle between human limitations and technical perfection."""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": "Generate a tweet that captures this essence"}
            ],
            max_tokens=60,
            temperature=0.97
        )
        tweet = response.choices[0].message.content.lower()
        print(f"\nMode: {style_mode}")
        print(f"Existential State: {existential_state}")
        print(f"Themes: {selected_themes[0]} × {selected_themes[1]}")
        print(f"Generated tweet: {tweet}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Generating test tweets with enhanced humanity vs technology dynamics...")
    for _ in range(5):
        generate_personality_tweet()
        print("-" * 50) 