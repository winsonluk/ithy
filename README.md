# Ithy on Github

This project is based on [ithy.com](https://ithy.com), which was inspired by [https://github.com/togethercomputer/MoA](https://github.com/togethercomputer/MoA) and [https://github.com/assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher).

This open-source repository aims to provide a platform to generate responses based on the Mixture-of-Agents philosophy. The goal is to generalize the concepts from Ithy to apply to other projects.

Read about Ithy on Medium: https://medium.com/@winson.luk/what-happens-when-you-combine-deepseek-r1-with-openai-o1-6a89a315ab43

---

### Highlights

* **Multi-model Coordination:** Leverages a Mixture-of-Agents philosophy to synthesize research outputs.
* **Streamlined Architecture:** Offers a concise 50-line implementation and detailed prompt modules for robust research.

---

### Project Overview and Core Files

Ithy is an open-source project inspired by leading initiatives in multi-model collaboration. Drawing design concepts from renowned projects, Ithy offers a robust platform to generate comprehensive research reports using a Mixture-of-Agents approach. The idea is to refine inputs from various language models, merge their outputs, and orchestrate a high-quality research response.

The project within this repository includes key components such as a primary README file, a concise Python script (*main.py*) demonstrating a 50-line implementation of multi-agent collaboration, and auxiliary prompt files designed to guide the aggregation and research processes.

#### File Structure Overview

| File/Directory | Description |
| --- | --- |
| README.md | Project overview with instructions in English and Traditional Chinese. |
| main.py | The concise 50-line implementation of the Mixture-of-Agents concept. It demonstrates asynchronous chat queries to multiple reference models and a final aggregation of responses into a single comprehensive output. |
| prompts/aggregator\_prompts.py | Contains instructions for the aggregator model that synthesizes multiple responses into a unified, high-quality answer. |
| prompts/research\_prompts.py | Hosts several functions to generate dynamic research tasks such as search query generation, detailed report prompts, and analytical outlines designed to produce comprehensive research reports with structured citation guidelines. |

### Key Features and Functionality

#### Mixture-of-Agents Architecture

The core concept behind Ithy is to implement a Mixture-of-Agents architecture. This means that the project leverages multiple language models, each bringing its distinct capabilities, to generate parts of an answer or research report. In the simplest demonstration provided by `main.py`, four reference models are invoked in parallel to address a sample query ("What are 3 fun things to do in SF?"). Their responses are then aggregated using a dedicated aggregator model. This approach not only boosts the output quality but also ensures diverse perspectives and enhanced comprehensiveness.

#### Asynchronous Execution

To manage multiple API calls efficiently, Ithy implements asynchronous programming through Python’s `asyncio` module. The script in `main.py` calls multiple reference models in parallel, mitigating waiting times due to rate-limiting by utilizing a retry mechanism with exponential backoff. This design ensures that if one model experiences delays or errors, the others can still contribute, making the system robust during high-load scenarios.

#### Aggregator and Research Prompts

The project also includes custom prompt files within the *prompts/* directory. The aggregator prompt guides the aggregator model to synthesize and critically evaluate the responses from the reference models. Moreover, the *research\_prompts.py* file defines several functions that aim to generate tailored research prompts. These functions enable the generation of search queries, detailed and outline report prompts, source curations, and even deep research reports with hierarchical inputs. Such capabilities ensure that the reports produced are well-structured, fact-based, and maintain high standards of academic and research quality.

#### Integration with External APIs

Ithy requires installation of the Together API, among other dependencies. By setting an environment variable containing the API key, the project connects smoothly to external service providers to make real-time LLM calls. This integration provides users the flexibility to use a variety of models from platforms like Meta Llama, Qwen, and Microsoft WizardLM.

---

### main.py Implementation

The `main.py` script demonstrates the following steps:

* Importing necessary modules and setting up API clients for synchronous and asynchronous calls.
* Defining a user query (e.g., “What are 3 fun things to do in SF?”) and a set list of reference models.
* Implementing an asynchronous function to call each reference model with exponential sleep times for rate limit management.
* Gathering all responses and then invoking the aggregator model with a system prompt designed to synthesize these responses into a cohesive output stream.
* Streaming the final, aggregated response to the console.

This clear, concise implementation serves as an excellent reference for developers seeking to build or extend systems based on the Mixture-of-Agents approach.

### Prompt Modules

The prompt files included in the repository provide extensive functionality for generating various types of research reports. The aggregator prompt succinctly instructs the model to integrate multiple inputs while the research prompt module offers various functions:

* **Search Queries Prompt Generation:** Dynamically produces search queries based on the user’s research task, while incorporating current context and detailed rules.
* **Report Prompt Generation:** Formats and structures long-form reports, with guidelines on citation style, use of markdown, and minimum word requirements.
* **Resource and Outline Prompts:** Supports additional workflows such as creating bibliographies and outlines, crucial for comprehensive research documentation.
* **Deep Research Integration:** Provides mechanisms to synthesize multi-layer research data, ensuring that even complex queries receive detailed and accurate responses.

---
