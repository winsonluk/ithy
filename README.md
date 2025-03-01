# Ithy

Ithy borrows from [https://github.com/togethercomputer/MoA](https://github.com/togethercomputer/MoA) and [https://github.com/assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher).

The Ithy open-source project aims to provide a platform to generate research reports based on the Mixture-of-Agents philosophy.

Ithy Project Documentation
==========================

### An Open-Source AI Aggregator

---

Highlights
----------

* **Multi-model Coordination:** Leverages a Mixture-of-Agents philosophy to synthesize research outputs.
* **Streamlined Architecture:** Offers a concise 50-line implementation and detailed prompt modules for robust research.

---

English Version README.md
-------------------------

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

正體中文版本 README.md
----------------

### 專案概述與核心檔案

Ithy 是一個開源專案，其設計靈感來自於先進的多模型協作概念。該專案目標是通過「混合智能體」（Mixture-of-Agents）的理念，生成結構化且全面的研究報告。Ithy 利用多個語言模型的優勢，對各自的回應進行融合，並最終綜合成一個高質量的回應。

此專案包含了多個關鍵組件，如專案說明文件（README.md）、展示 50 行代碼實現混合智能體概念的 `main.py` 檔案，以及在 *prompts/* 目錄下的各類提示檔案，這些提示檔案用來指導聚合模型和研究任務的生成過程。

#### 檔案結構概覽

| 檔案/資料夾 | 說明 |
| --- | --- |
| README.md | 專案概述與使用說明，提供英文及正體中文版本。 |
| main.py | 展示混合智能體概念的 50 行程式碼，採用非同步呼叫多個參考模型並將結果聚合成終極回應。 |
| prompts/aggregator\_prompts.py | 包含聚合模型的提示，指導其整合各個模型所給出的回應成一個高質量回應。 |
| prompts/research\_prompts.py | 定義了產生研究任務提示的多個函數，這些提示涵蓋生成搜尋查詢、詳細報告大綱、資源推薦等多種功能。 |

### 主要特色與功能

#### 混合智能體架構

Ithy 專案的核心概念在於實現混合智能體架構。透過整合多個專門的語言模型，每個模型都能針對部分問題提供獨到的見解。以 `main.py` 為例，系統同時邀請四個參考模型來回答範例查詢「What are 3 fun things to do in SF?」，然後透過一個專用的聚合器模型將各個回應整合成一個高質量的最終答案。這種方式不僅提升了回應的多樣性，亦確保了結果的全面性。

#### 非同步執行

為了有效地處理多個 API 呼叫，Ithy 採用了 Python 的 `asyncio` 模組來實現非同步編程。這使得多個參考模型能夠並行處理查詢，即使遇到速率限制問題，也能通過退避重試機制保持穩定運行。當某一模型遇到延遲或錯誤時，其餘模型依然能持續提供輸出，確保整體系統的穩健性。

#### 聚合器與研究提示

該專案在 *prompts/* 目錄下包含多個提示模板。聚合提示引導聚合器模型對來自各參考模型的回應進行整合和關鍵性評估。而 `research_prompts.py` 中包含的各種函數則支持生成搜尋查詢、詳細報告提示、以及研究資料組織的工作。這些提示幫助用戶生成結構化、事實依據充分的研究報告，並包含正確的引用和文獻清單。

#### API 整合與擴充性

Ithy 依賴外部的 Together API 以及其他相關依賴項。通過設定環境變數中的 API 金鑰，使用者可以方便地與不同平台上的語言模型（如 Meta Llama、Qwen、Microsoft WizardLM 等）進行即時交互。這一整合方案讓使用者能根據實際需求選擇與配置最合適的模型。

---

In-Depth Look at the Code
-------------------------

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
