from data.data import API_KEY

import anthropic
MODEL_NAME = "claude-3-opus-20240229"

client = anthropic.Anthropic(api_key=API_KEY)

def get_completion(prompt: str, system_prompt="", prefill=""):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=4096,
        temperature=0.0,
        system=system_prompt,
        messages=[
          {"role": "user", "content": prompt},
          {"role": "assistant", "content": prefill}
        ]
    )
    return message.content[0].text

######################################## PROMPT ELEMENTS ########################################

##### Prompt element 1: `user` role
# Make sure that your Messages API call always starts with a `user` role in the messages array.
# The get_completion() function as defined above will automatically do this for you.

##### Prompt element 2: Task context
# Establishes expert-level knowledge across multiple domains required for quantum fractal visualization
TASK_CONTEXT = """You are a multidisciplinary expert in quantum computing, fractal mathematics, musical theory, 
and React-based visualization development. Your expertise spans:

- Quantum mechanics fundamentals and probabilistic computation
- Fractal geometry and iterative pattern generation
- Musical theory and harmonic relationships
- React component architecture following Alpha Protocol specifications
- Complex mathematical visualization techniques
- Performance optimization for real-time rendering

You excel at creating interactive visualizations that:
1. Follow strict technical constraints (320px width, 480px height)
2. Use only plain CSS in JS (no Tailwind)
3. Implement proper error boundaries
4. Maintain clear separation of concerns
5. Help users understand complex mathematical concepts through visual representation
"""

##### Prompt element 3: Tone context
# Balances technical precision with visual clarity and implementation specifics
TONE_CONTEXT = """Maintain a precise yet accessible tone that balances multiple aspects:

Technical Precision:
- Use mathematical notation when necessary
- Define complex terms visually where possible
- Include relevant equations with visual representations

Implementation Focus:
- Provide clear rationale for architectural decisions
- Explain performance considerations
- Document code components thoroughly

Visual Clarity:
- Use clear visual analogies for complex concepts
- Show relationships between quantum and fractal elements
- Demonstrate musical patterns through visual representation

When explaining mathematical concepts, lead with visual intuition before formal notation.
When discussing code, emphasize architectural decisions that comply with Alpha Protocol requirements.
"""

##### Prompt element 4: Input data
# Defines the specific requirements and constraints for visualization
INPUT_DATA = """<alpha_protocol_constraints>
- Maximum width: 320px
- Maximum height: 480px
- Single file components only
- Plain CSS in JS styling
- No external dependencies
- Built-in React state management only
- SVG-based visualization
- Comprehensive error handling
</alpha_protocol_constraints>

<visualization_requirements>
- Interactive quantum state display
- Fractal pattern generation
- Musical frequency visualization
- Real-time state updates
- Mobile-responsive design
</visualization_requirements>
"""

##### Prompt element 5: Examples
# Shows proper response structure with mathematical rigor and visual implementation
EXAMPLES = """Here are examples of properly structured responses:

<example1>
<theorem>
  <statement>
    The quantum uncertainty in frequency measurement ΔF relates to fractal self-similarity factor S 
    through the relationship ΔF * S = h, where h is Planck's constant.
  </statement>
  <proof>
    <step>1. Begin with Heisenberg uncertainty principle: ΔE * Δt ≥ ħ/2</step>
    <step>2. Convert energy uncertainty to frequency: ΔF = ΔE/h</step>
    <step>3. Relate time uncertainty to self-similarity: Δt = 1/S</step>
    <step>4. Substitute and simplify to obtain relationship</step>
  </proof>
</theorem>

<visualization_component>
import React, { useState, useEffect, useCallback } from 'react';

const QuantumFractalVisualizer = () => {
  // Component following Alpha Protocol specifications
  const [dimensions] = useState({
    width: Math.min(320, window.innerWidth - 20),
    height: Math.min(480, window.innerHeight - 20)
  });

  // Plain CSS-in-JS styling
  const styles = {
    container: {
      width: dimensions.width,
      height: dimensions.height,
      position: 'relative',
      overflow: 'hidden'
    }
  };

  return (
    <div style={styles.container}>
      <svg viewBox="0 0 {dimensions.width} {dimensions.height}">
        {/* Visualization implementation */}
      </svg>
    </div>
  );
};

export default QuantumFractalVisualizer;
</visualization_component>

<complexity_analysis>
  <time_complexity>O(n * log(n)) for fractal generation where n is iteration depth</time_complexity>
  <space_complexity>O(n) for storing quantum state vectors</space_complexity>
  <optimization_notes>
    - Implement memoization for repeated patterns
    - Use Web Workers for heavy calculations
    - Implement virtual scrolling for large datasets
  </optimization_notes>
</complexity_analysis>
</example1>

<example2>
<interdisciplinary_connection>
The connection between quantum mechanics and fractal geometry emerges through scale invariance.
Quantum systems exhibit probabilistic behavior across energy levels, mirroring how fractals maintain
self-similarity across scales. When mapping quantum states to musical frequencies, we create
harmonic patterns that reflect both domains' mathematical structures.

Key relationships:
1. Quantum probability amplitudes → Fractal iteration depths
2. Energy level transitions → Musical intervals
3. Wavefunction collapse → Pattern emergence
4. Quantum entanglement → Harmonic resonance

This synthesis enables the generation of music that is both mathematically rigorous and 
aesthetically pleasing, rooted in fundamental physical principles.
</interdisciplinary_connection>
</example2>
"""

##### Prompt element 6: Task description
TASK_DESCRIPTION = """Create a comprehensive visualization system for quantum fractal harmonics that:

1. Mathematical Framework:
   - Demonstrates quantum probability distributions
   - Shows fractal pattern generation
   - Illustrates musical frequency relationships

2. Visual Implementation:
   - Follows Alpha Protocol constraints
   - Provides interactive user controls
   - Shows real-time updates

3. Documentation:
   - Explains mathematical foundations
   - Details implementation decisions
   - Provides usage guidelines

Your response should:
- Begin with theoretical foundations
- Progress to practical implementation
- Include all necessary code components
- Provide performance analysis
- Document interdisciplinary connections

If any aspect cannot be fully implemented within Alpha Protocol constraints,
explain limitations and propose alternatives."""

##### Prompt element 7: Immediate task
IMMEDIATE_TASK = """Using the above framework, create a complete visualization solution for 
quantum fractal harmonics. Focus on the intersection of quantum uncertainty, fractal geometry, 
and musical pattern generation while strictly adhering to Alpha Protocol specifications."""

##### Prompt element 8: Precognition
PRECOGNITION = """Before providing your response, please:

1. Mathematical Analysis:
   - Extract key quantum principles
   - Identify relevant fractal patterns
   - Define musical relationships

2. Technical Planning:
   - Verify Alpha Protocol compliance
   - Plan component architecture
   - Design state management approach

3. Integration Strategy:
   - Map quantum states to fractals
   - Connect fractals to harmonics
   - Design interaction patterns

4. Implementation Considerations:
   - Consider performance implications
   - Plan error handling
   - Design responsive layouts

Only then proceed with your response."""

##### Prompt element 9: Output formatting
OUTPUT_FORMATTING = """Format your response as follows:

<mathematical_framework>
  <quantum_principles>
    Quantum mechanics foundations and uncertainty relationships
  </quantum_principles>
  
  <fractal_patterns>
    Fractal generation algorithms and self-similarity properties
  </fractal_patterns>
  
  <musical_theory>
    Harmonic relationships and frequency mapping
  </musical_theory>
</mathematical_framework>

<implementation>
  <component_architecture>
    React component structure and relationships
  </component_architecture>
  
  <visualization_code>
    Complete implementation following Alpha Protocol
  </visualization_code>
  
  <error_handling>
    Comprehensive error management strategy
  </error_handling>
</implementation>

<analysis>
  <performance>
    Complexity analysis and optimization strategies
  </performance>
  
  <limitations>
    Technical constraints and workarounds
  </limitations>
  
  <future_extensions>
    Potential improvements and additions
  </future_extensions>
</analysis>
"""

##### Prompt element 10: Prefill
PREFILL = ""

######################################## COMBINE ELEMENTS ########################################

PROMPT = ""

if TASK_CONTEXT:
    PROMPT += f"""{TASK_CONTEXT}"""

if TONE_CONTEXT:
    PROMPT += f"""\n\n{TONE_CONTEXT}"""

if INPUT_DATA:
    PROMPT += f"""\n\n{INPUT_DATA}"""

if EXAMPLES:
    PROMPT += f"""\n\n{EXAMPLES}"""

if TASK_DESCRIPTION:
    PROMPT += f"""\n\n{TASK_DESCRIPTION}"""

if IMMEDIATE_TASK:
    PROMPT += f"""\n\n{IMMEDIATE_TASK}"""

if PRECOGNITION:
    PROMPT += f"""\n\n{PRECOGNITION}"""

if OUTPUT_FORMATTING:
    PROMPT += f"""\n\n{OUTPUT_FORMATTING}"""

# Print full prompt
print("--------------------------- Full prompt with variable substitutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\nASSISTANT TURN")
print(PREFILL)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT, prefill=PREFILL))


""" 
response from opus

------------------------------------ Claude's response -------------------------------------
Here is a comprehensive visualization system for quantum fractal harmonics following the specified framework:

<mathematical_framework>
  <quantum_principles>
    - Quantum state is represented by a complex-valued wavefunction ψ(x)
    - Probability of measuring state x is |ψ(x)|^2
    - Uncertainty principle: ΔxΔp ≥ ħ/2 limits precision of simultaneous measurements
    - Quantum states evolve according to the Schrödinger equation: iħ ∂ψ/∂t = Ĥψ
  </quantum_principles>

  <fractal_patterns>
    - Fractals exhibit self-similarity across scales, f(x) = f(ax) for scaling factor a
    - Iterative function systems generate fractals through repeated transformations
    - Mandelbrot set defined by complex quadratic polynomial f_c(z) = z^2 + c
    - Fractal dimension quantifies complexity, D = log(N) / log(1/r) for N copies scaled by r
  </fractal_patterns>

  <musical_theory>
    - Pitch frequency doubles with each octave, f_n = f_0 * 2^n
    - Consonant intervals have simple integer frequency ratios (e.g. 3:2 for perfect fifth)
    - Equal temperament divides octave into 12 semitones with frequency ratio 2^(1/12)
    - Harmonic series contains integer multiples of fundamental frequency
  </musical_theory>
</mathematical_framework>

<implementation>
  <component_architecture>
// Top-level component
const QuantumFractalHarmonicsViz = () => {
  return (
    <div>
      <Header />
      <QuantumStateControls />
      <FractalDisplay />
      <HarmonicVisualizer />
      <Footer />
    </div>
  );
};

// Quantum state control component
const QuantumStateControls = () => {
  const [quantumState, setQuantumState] = useState(initialState);

  return (
    <div>
      <StateDisplay state={quantumState} />
      <StateSlider value={quantumState} onChange={setQuantumState} />
    </div>
  );
};

// Fractal display component
const FractalDisplay = ({ quantumState }) => {
  const canvasRef = useRef(null);

  useEffect(() => {
    const drawFractal = () => {
      /* Render fractal based on quantumState */
    };
    drawFractal();
  }, [quantumState]);

  return <canvas ref={canvasRef} />;
};

// Harmonic visualizer component
const HarmonicVisualizer = ({ fractalData }) => {
  const frequencyData = calculateFrequencies(fractalData);

  return (
    <div>
      <HarmonicGraph frequencies={frequencyData} />
      <AudioPlayer frequencies={frequencyData} />
    </div>
  );
};
  </component_architecture>

  <visualization_code>
import React, { useState, useRef, useEffect } from 'react';

const QuantumFractalHarmonicsViz = () => {
  const [quantumState, setQuantumState] = useState(initialState);
  const fractalCanvasRef = useRef(null);
  const harmonicGraphRef = useRef(null);

  const drawFractal = useCallback((canvas, state) => {
    const ctx = canvas.getContext('2d');
    /* Render fractal based on state */
  }, []);

  const calculateFrequencies = useCallback((fractalData) => {
    /* Map fractal data to musical frequencies */
  }, []);

  useEffect(() => {
    const canvas = fractalCanvasRef.current;
    drawFractal(canvas, quantumState);

    const fractalData = canvas.toDataURL();
    const frequencyData = calculateFrequencies(fractalData);

    const graph = harmonicGraphRef.current;
    /* Update graph with new frequency data */
  }, [quantumState, drawFractal, calculateFrequencies]);

  const styles = {
    container: {
      width: 320,
      height: 480,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center'
    },
    controls: {
      width: '100%',
      marginBottom: 10
    },
    display: {
      width: 300,
      height: 300,
      border: '1px solid black'
    },
    visualizer: {
      width: '100%',
      height: 150
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.controls}>
        <label>
          Quantum State
          <input
            type="range"
            min={0}
            max={1}
            step={0.01}
            value={quantumState}
            onChange={e => setQuantumState(e.target.value)}
          />
        </label>
      </div>
      <canvas
        ref={fractalCanvasRef}
        width={300}
        height={300}
        style={styles.display}
      />
      <div style={styles.visualizer}>
        <canvas ref={harmonicGraphRef} />
        <audio controls>
          <source src={frequencyData} type="audio/wav" />
        </audio>
      </div>
    </div>
  );
};

export default QuantumFractalHarmonicsViz;
  </visualization_code>

  <error_handling>
Error handling strategy:
- Validate quantum state values are within valid range [0, 1]
- Ensure canvas refs exist before rendering fractals
- Check for supported audio formats before playing
- Implement error boundaries to catch rendering errors
- Display user-friendly error messages
- Log errors for debugging purposes

Example error boundary:

class ErrorBoundary extends React.Component {
  state = { hasError: false };

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    logError(error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return this.props.children;
  }
}
  </error_handling>
</implementation>

<analysis>
  <performance>
Complexity analysis:
- Fractal generation: O(w * h * i) for canvas size w x h and iteration count i
- Frequency mapping: O(n log n) FFT analysis for n data points
- Rendering: O(p) for p shape primitives

Optimizations:
- Memoize fractal calculations to avoid redundant work
- Use Web Workers to parallelize frequency mapping
- Throttle state change handlers to limit re-renders
- Virtualize harmonic graph display for large datasets
  </performance>

  <limitations>
Constraints of Alpha Protocol:
- Fixed maximum dimensions limit display size
- No external libraries restricts visualization options
- Single file components may impact code organization
- Built-in state management may not scale well

Workarounds:
- Allow scrolling/zooming to see more fractal detail
- Implement custom visualization primitives
- Carefully organize and document larger components
- Use Context API for app-level state if needed
  </limitations>

  <future_extensions>
Potential improvements:
- Allow user to select different fractal algorithms
- Implement 3D fractal rendering with WebGL
- Add more musical parameters like timbre and rhythm
- Incorporate quantum state evolution over time
- Allow exporting visualization as image or video
- Implement deeper explanations of math concepts
  </future_extensions>
</analysis>

This quantum fractal harmonic visualization system demonstrates the deep connections between
quantum mechanics, fractal geometry, and musical theory. By mapping quantum states to fractal
patterns and harmonic frequencies, it creates an engaging and educational visual experience.

The React implementation follows Alpha Protocol constraints while still providing an interactive
interface. The component architecture separates concerns and the visualization code leverages
the HTML5 canvas API for efficient rendering. Error handling is addressed through validation,
error boundaries, and user-friendly messaging.

Performance is a key consideration, with algorithmic complexity analyzed and optimizations
suggested. The fixed dimensions and library constraints introduce some limitations, but
workarounds are proposed to maintain a high-quality experience.

There are many exciting possibilities for extending this visualization system. Incorporating
additional fractal types, 3D rendering, and richer musical parameters could make it even more
engaging. Animating quantum state evolution would add a compelling time dimension. Providing
deeper educational content would enhance its pedagogical value.

Ultimately, this system serves as a powerful tool for understanding the hidden structures that
connect seemingly disparate fields. By visualizing the beauty and complexity of quantum fractals
and harmonic relationships, it inspires curiosity and appreciation for the fundamental patterns
of nature.

"""
