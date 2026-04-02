Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/_cpp_gen/executor.md

* Executor

# Executor[#](#executor "Link to this heading")

## cacheCommunicator.h[#](#cachecommunicator-h "Link to this heading")

namespace tensorrt\_llm[#](#_CPPv412tensorrt_llm "Link to this definition")
:   namespace executor[#](#_CPPv4N12tensorrt_llm8executorE "Link to this definition")
    :   namespace kv\_cache[#](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "Link to this definition")
        :   class Connection[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10ConnectionE "Link to this definition")
            :   Public Functions

                virtual ~Connection() = default[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10ConnectionD0Ev "Link to this definition")

                virtual void send( : *[DataContext](#_CPPv4N12tensorrt_llm8executor8kv_cache11DataContextE "tensorrt_llm::executor::kv_cache::DataContext") const &ctx*, : *void const \*data*, : *size\_t size*, ) const = 0[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache10Connection4sendERK11DataContextPKv6size_t "Link to this definition")

                virtual void recv( : *[DataContext](#_CPPv4N12tensorrt_llm8executor8kv_cache11DataContextE "tensorrt_llm::executor::kv_cache::DataContext") const &ctx*, : *void \*data*, : *size\_t size*, ) const = 0[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache10Connection4recvERK11DataContextPv6size_t "Link to this definition")

                inline virtual bool isThreadSafe() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache10Connection12isThreadSafeEv "Link to this definition")

            class ConnectionManager[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17ConnectionManagerE "Link to this definition")
            :   Public Functions

                virtual ~ConnectionManager() = default[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17ConnectionManagerD0Ev "Link to this definition")

                virtual [Connection](#_CPPv4N12tensorrt_llm8executor8kv_cache10ConnectionE "tensorrt_llm::executor::kv_cache::Connection") const \*recvConnect( : *[DataContext](#_CPPv4N12tensorrt_llm8executor8kv_cache11DataContextE "tensorrt_llm::executor::kv_cache::DataContext") const &ctx*, : *void \*data*, : *size\_t size*, ) = 0[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17ConnectionManager11recvConnectERK11DataContextPv6size_t "Link to this definition")

                virtual std::vector<[Connection](#_CPPv4N12tensorrt_llm8executor8kv_cache10ConnectionE "tensorrt_llm::executor::kv_cache::Connection") const\*> getConnections( : *[CommState](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommStateE "tensorrt_llm::executor::kv_cache::CommState") const &state*, ) = 0[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17ConnectionManager14getConnectionsERK9CommState "Link to this definition")

                virtual [CommState](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommStateE "tensorrt_llm::executor::kv_cache::CommState") const &getCommState() const = 0[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache17ConnectionManager12getCommStateEv "Link to this definition")

            struct DataContext[#](#_CPPv4N12tensorrt_llm8executor8kv_cache11DataContextE "Link to this definition")
            :   Public Functions

                inline explicit DataContext(*int tag*)[#](#_CPPv4N12tensorrt_llm8executor8kv_cache11DataContext11DataContextEi "Link to this definition")

                inline int getTag() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache11DataContext6getTagEv "Link to this definition")

                Private Members

                int const mTag[#](#_CPPv4N12tensorrt_llm8executor8kv_cache11DataContext4mTagE "Link to this definition")

## serialization.h[#](#serialization-h "Link to this heading")

namespace tensorrt\_llm
:   namespace executor
    :   class Serialization[#](#_CPPv4N12tensorrt_llm8executor13SerializationE "Link to this definition")
        :   Public Static Functions

            static [RequestPerfMetrics](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetricsE "tensorrt_llm::executor::RequestPerfMetrics")::[TimePoint](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics9TimePointE "tensorrt_llm::executor::RequestPerfMetrics::TimePoint") deserializeTimePoint( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization20deserializeTimePointERNSt7istreamE "Link to this definition")

            static void serialize( : *[RequestPerfMetrics](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetricsE "tensorrt_llm::executor::RequestPerfMetrics")::[TimePoint](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics9TimePointE "tensorrt_llm::executor::RequestPerfMetrics::TimePoint") const &tp*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKN18RequestPerfMetrics9TimePointERNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[RequestPerfMetrics](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetricsE "tensorrt_llm::executor::RequestPerfMetrics")::[TimePoint](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics9TimePointE "tensorrt_llm::executor::RequestPerfMetrics::TimePoint") const&*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERKN18RequestPerfMetrics9TimePointE "Link to this definition")

            static [RequestPerfMetrics](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetricsE "tensorrt_llm::executor::RequestPerfMetrics") deserializeRequestPerfMetrics( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization29deserializeRequestPerfMetricsERNSt7istreamE "Link to this definition")

            static void serialize( : *[RequestPerfMetrics](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetricsE "tensorrt_llm::executor::RequestPerfMetrics") const &metrics*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK18RequestPerfMetricsRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[RequestPerfMetrics](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetricsE "tensorrt_llm::executor::RequestPerfMetrics") const &metrics*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK18RequestPerfMetrics "Link to this definition")

            static [SamplingConfig](#_CPPv4N12tensorrt_llm8executor14SamplingConfigE "tensorrt_llm::executor::SamplingConfig") deserializeSamplingConfig(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization25deserializeSamplingConfigERNSt7istreamE "Link to this definition")

            static void serialize(*[SamplingConfig](#_CPPv4N12tensorrt_llm8executor14SamplingConfigE "tensorrt_llm::executor::SamplingConfig") const &config*, *std::ostream &os*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK14SamplingConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[SamplingConfig](#_CPPv4N12tensorrt_llm8executor14SamplingConfigE "tensorrt_llm::executor::SamplingConfig") const &config*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK14SamplingConfig "Link to this definition")

            static [OutputConfig](#_CPPv4N12tensorrt_llm8executor12OutputConfigE "tensorrt_llm::executor::OutputConfig") deserializeOutputConfig(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization23deserializeOutputConfigERNSt7istreamE "Link to this definition")

            static void serialize(*[OutputConfig](#_CPPv4N12tensorrt_llm8executor12OutputConfigE "tensorrt_llm::executor::OutputConfig") const &config*, *std::ostream &os*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK12OutputConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[OutputConfig](#_CPPv4N12tensorrt_llm8executor12OutputConfigE "tensorrt_llm::executor::OutputConfig") const &config*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK12OutputConfig "Link to this definition")

            static [AdditionalModelOutput](#_CPPv4N12tensorrt_llm8executor21AdditionalModelOutputE "tensorrt_llm::executor::AdditionalModelOutput") deserializeAdditionalModelOutput( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization32deserializeAdditionalModelOutputERNSt7istreamE "Link to this definition")

            static void serialize( : *[AdditionalModelOutput](#_CPPv4N12tensorrt_llm8executor21AdditionalModelOutputE "tensorrt_llm::executor::AdditionalModelOutput") const &additionalModelOutput*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK21AdditionalModelOutputRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize( : *[AdditionalModelOutput](#_CPPv4N12tensorrt_llm8executor21AdditionalModelOutputE "tensorrt_llm::executor::AdditionalModelOutput") const &additionalModelOutput*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK21AdditionalModelOutput "Link to this definition")

            static [ExternalDraftTokensConfig](#_CPPv4N12tensorrt_llm8executor25ExternalDraftTokensConfigE "tensorrt_llm::executor::ExternalDraftTokensConfig") deserializeExternalDraftTokensConfig( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization36deserializeExternalDraftTokensConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[ExternalDraftTokensConfig](#_CPPv4N12tensorrt_llm8executor25ExternalDraftTokensConfigE "tensorrt_llm::executor::ExternalDraftTokensConfig") const &config*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK25ExternalDraftTokensConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[ExternalDraftTokensConfig](#_CPPv4N12tensorrt_llm8executor25ExternalDraftTokensConfigE "tensorrt_llm::executor::ExternalDraftTokensConfig") const &config*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK25ExternalDraftTokensConfig "Link to this definition")

            static [PromptTuningConfig](#_CPPv4N12tensorrt_llm8executor18PromptTuningConfigE "tensorrt_llm::executor::PromptTuningConfig") deserializePromptTuningConfig( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization29deserializePromptTuningConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[PromptTuningConfig](#_CPPv4N12tensorrt_llm8executor18PromptTuningConfigE "tensorrt_llm::executor::PromptTuningConfig") const &config*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK18PromptTuningConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[PromptTuningConfig](#_CPPv4N12tensorrt_llm8executor18PromptTuningConfigE "tensorrt_llm::executor::PromptTuningConfig") const &config*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK18PromptTuningConfig "Link to this definition")

            static [MultimodalInput](#_CPPv4N12tensorrt_llm8executor15MultimodalInputE "tensorrt_llm::executor::MultimodalInput") deserializeMultimodalInput(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization26deserializeMultimodalInputERNSt7istreamE "Link to this definition")

            static void serialize( : *[MultimodalInput](#_CPPv4N12tensorrt_llm8executor15MultimodalInputE "tensorrt_llm::executor::MultimodalInput") const &multimodalInput*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK15MultimodalInputRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[MultimodalInput](#_CPPv4N12tensorrt_llm8executor15MultimodalInputE "tensorrt_llm::executor::MultimodalInput") const &multimodalInput*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK15MultimodalInput "Link to this definition")

            static [MropeConfig](#_CPPv4N12tensorrt_llm8executor11MropeConfigE "tensorrt_llm::executor::MropeConfig") deserializeMropeConfig(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization22deserializeMropeConfigERNSt7istreamE "Link to this definition")

            static void serialize(*[MropeConfig](#_CPPv4N12tensorrt_llm8executor11MropeConfigE "tensorrt_llm::executor::MropeConfig") const &config*, *std::ostream &os*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK11MropeConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[MropeConfig](#_CPPv4N12tensorrt_llm8executor11MropeConfigE "tensorrt_llm::executor::MropeConfig") const &config*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK11MropeConfig "Link to this definition")

            static [LoraConfig](#_CPPv4N12tensorrt_llm8executor10LoraConfigE "tensorrt_llm::executor::LoraConfig") deserializeLoraConfig(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization21deserializeLoraConfigERNSt7istreamE "Link to this definition")

            static void serialize(*[LoraConfig](#_CPPv4N12tensorrt_llm8executor10LoraConfigE "tensorrt_llm::executor::LoraConfig") const &config*, *std::ostream &os*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK10LoraConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[LoraConfig](#_CPPv4N12tensorrt_llm8executor10LoraConfigE "tensorrt_llm::executor::LoraConfig") const &config*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK10LoraConfig "Link to this definition")

            static [kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[CommState](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommStateE "tensorrt_llm::executor::kv_cache::CommState") deserializeCommState(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization20deserializeCommStateERNSt7istreamE "Link to this definition")

            static void serialize( : *[kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[CommState](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommStateE "tensorrt_llm::executor::kv_cache::CommState") const &state*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKN8kv_cache9CommStateERNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[CommState](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommStateE "tensorrt_llm::executor::kv_cache::CommState") const &state*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERKN8kv_cache9CommStateE "Link to this definition")

            static [kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[SocketState](#_CPPv4N12tensorrt_llm8executor8kv_cache11SocketStateE "tensorrt_llm::executor::kv_cache::SocketState") deserializeSocketState(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization22deserializeSocketStateERNSt7istreamE "Link to this definition")

            static void serialize( : *[kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[SocketState](#_CPPv4N12tensorrt_llm8executor8kv_cache11SocketStateE "tensorrt_llm::executor::kv_cache::SocketState") const &state*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKN8kv_cache11SocketStateERNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[SocketState](#_CPPv4N12tensorrt_llm8executor8kv_cache11SocketStateE "tensorrt_llm::executor::kv_cache::SocketState") const &state*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERKN8kv_cache11SocketStateE "Link to this definition")

            static [kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[AgentState](#_CPPv4N12tensorrt_llm8executor8kv_cache10AgentStateE "tensorrt_llm::executor::kv_cache::AgentState") deserializeAgentState(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization21deserializeAgentStateERNSt7istreamE "Link to this definition")

            static void serialize( : *[kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[AgentState](#_CPPv4N12tensorrt_llm8executor8kv_cache10AgentStateE "tensorrt_llm::executor::kv_cache::AgentState") const &state*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKN8kv_cache10AgentStateERNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[AgentState](#_CPPv4N12tensorrt_llm8executor8kv_cache10AgentStateE "tensorrt_llm::executor::kv_cache::AgentState") const &state*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERKN8kv_cache10AgentStateE "Link to this definition")

            static [kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[CacheState](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheStateE "tensorrt_llm::executor::kv_cache::CacheState") deserializeCacheState(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization21deserializeCacheStateERNSt7istreamE "Link to this definition")

            static void serialize( : *[kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[CacheState](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheStateE "tensorrt_llm::executor::kv_cache::CacheState") const &state*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKN8kv_cache10CacheStateERNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[CacheState](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheStateE "tensorrt_llm::executor::kv_cache::CacheState") const &state*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERKN8kv_cache10CacheStateE "Link to this definition")

            static [DataTransceiverState](#_CPPv4N12tensorrt_llm8executor20DataTransceiverStateE "tensorrt_llm::executor::DataTransceiverState") deserializeDataTransceiverState( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization31deserializeDataTransceiverStateERNSt7istreamE "Link to this definition")

            static [DataTransceiverState](#_CPPv4N12tensorrt_llm8executor20DataTransceiverStateE "tensorrt_llm::executor::DataTransceiverState") deserializeDataTransceiverState( : *std::vector<char> &buffer*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization31deserializeDataTransceiverStateERNSt6vectorIcEE "Link to this definition")

            static void serialize( : *[DataTransceiverState](#_CPPv4N12tensorrt_llm8executor20DataTransceiverStateE "tensorrt_llm::executor::DataTransceiverState") const &dataTransceiverState*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK20DataTransceiverStateRNSt7ostreamE "Link to this definition")

            static std::vector<char> serialize( : *[DataTransceiverState](#_CPPv4N12tensorrt_llm8executor20DataTransceiverStateE "tensorrt_llm::executor::DataTransceiverState") const &dataTransceiverState*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK20DataTransceiverState "Link to this definition")

            static size\_t serializedSize( : *[DataTransceiverState](#_CPPv4N12tensorrt_llm8executor20DataTransceiverStateE "tensorrt_llm::executor::DataTransceiverState") const &dataTransceiverState*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK20DataTransceiverState "Link to this definition")

            static [ContextPhaseParams](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsE "tensorrt_llm::executor::ContextPhaseParams") deserializeContextPhaseParams( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization29deserializeContextPhaseParamsERNSt7istreamE "Link to this definition")

            static void serialize( : *[ContextPhaseParams](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsE "tensorrt_llm::executor::ContextPhaseParams") const &contextPhaseParams*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK18ContextPhaseParamsRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize( : *[ContextPhaseParams](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsE "tensorrt_llm::executor::ContextPhaseParams") const &contextPhaseParams*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK18ContextPhaseParams "Link to this definition")

            static [Request](#_CPPv4N12tensorrt_llm8executor7RequestE "tensorrt_llm::executor::Request") deserializeRequest(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization18deserializeRequestERNSt7istreamE "Link to this definition")

            static void serialize(*[Request](#_CPPv4N12tensorrt_llm8executor7RequestE "tensorrt_llm::executor::Request") const &request*, *std::ostream &os*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK7RequestRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[Request](#_CPPv4N12tensorrt_llm8executor7RequestE "tensorrt_llm::executor::Request") const &request*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK7Request "Link to this definition")

            static [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") deserializeTensor(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization17deserializeTensorERNSt7istreamE "Link to this definition")

            static void serialize(*[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") const &tensor*, *std::ostream &os*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK6TensorRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") const &tensor*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK6Tensor "Link to this definition")

            static [SpeculativeDecodingFastLogitsInfo](#_CPPv4N12tensorrt_llm8executor33SpeculativeDecodingFastLogitsInfoE "tensorrt_llm::executor::SpeculativeDecodingFastLogitsInfo") deserializeSpecDecFastLogitsInfo( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization32deserializeSpecDecFastLogitsInfoERNSt7istreamE "Link to this definition")

            static void serialize( : *[SpeculativeDecodingFastLogitsInfo](#_CPPv4N12tensorrt_llm8executor33SpeculativeDecodingFastLogitsInfoE "tensorrt_llm::executor::SpeculativeDecodingFastLogitsInfo") const &info*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK33SpeculativeDecodingFastLogitsInfoRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize( : *[SpeculativeDecodingFastLogitsInfo](#_CPPv4N12tensorrt_llm8executor33SpeculativeDecodingFastLogitsInfoE "tensorrt_llm::executor::SpeculativeDecodingFastLogitsInfo") const &info*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK33SpeculativeDecodingFastLogitsInfo "Link to this definition")

            static [Result](#_CPPv4N12tensorrt_llm8executor6ResultE "tensorrt_llm::executor::Result") deserializeResult(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization17deserializeResultERNSt7istreamE "Link to this definition")

            static void serialize(*[Result](#_CPPv4N12tensorrt_llm8executor6ResultE "tensorrt_llm::executor::Result") const &result*, *std::ostream &os*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK6ResultRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[Result](#_CPPv4N12tensorrt_llm8executor6ResultE "tensorrt_llm::executor::Result") const &result*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK6Result "Link to this definition")

            static [AdditionalOutput](#_CPPv4N12tensorrt_llm8executor16AdditionalOutputE "tensorrt_llm::executor::AdditionalOutput") deserializeAdditionalOutput(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization27deserializeAdditionalOutputERNSt7istreamE "Link to this definition")

            static void serialize( : *[AdditionalOutput](#_CPPv4N12tensorrt_llm8executor16AdditionalOutputE "tensorrt_llm::executor::AdditionalOutput") const &additionalOutput*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK16AdditionalOutputRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize( : *[AdditionalOutput](#_CPPv4N12tensorrt_llm8executor16AdditionalOutputE "tensorrt_llm::executor::AdditionalOutput") const &additionalOutput*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK16AdditionalOutput "Link to this definition")

            static [Response](#_CPPv4N12tensorrt_llm8executor8ResponseE "tensorrt_llm::executor::Response") deserializeResponse(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization19deserializeResponseERNSt7istreamE "Link to this definition")

            static void serialize(*[Response](#_CPPv4N12tensorrt_llm8executor8ResponseE "tensorrt_llm::executor::Response") const &response*, *std::ostream &os*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK8ResponseRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[Response](#_CPPv4N12tensorrt_llm8executor8ResponseE "tensorrt_llm::executor::Response") const &response*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK8Response "Link to this definition")

            static std::vector<[Response](#_CPPv4N12tensorrt_llm8executor8ResponseE "tensorrt_llm::executor::Response")> deserializeResponses( : *std::vector<char> &buffer*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization20deserializeResponsesERNSt6vectorIcEE "Link to this definition")

            static std::vector<char> serialize( : *std::vector<[Response](#_CPPv4N12tensorrt_llm8executor8ResponseE "tensorrt_llm::executor::Response")> const &responses*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKNSt6vectorI8ResponseEE "Link to this definition")

            static [KvCacheConfig](#_CPPv4N12tensorrt_llm8executor13KvCacheConfigE "tensorrt_llm::executor::KvCacheConfig") deserializeKvCacheConfig(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization24deserializeKvCacheConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[KvCacheConfig](#_CPPv4N12tensorrt_llm8executor13KvCacheConfigE "tensorrt_llm::executor::KvCacheConfig") const &kvCacheConfig*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK13KvCacheConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[KvCacheConfig](#_CPPv4N12tensorrt_llm8executor13KvCacheConfigE "tensorrt_llm::executor::KvCacheConfig") const &kvCacheConfig*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK13KvCacheConfig "Link to this definition")

            static [DynamicBatchConfig](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfigE "tensorrt_llm::executor::DynamicBatchConfig") deserializeDynamicBatchConfig( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization29deserializeDynamicBatchConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[DynamicBatchConfig](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfigE "tensorrt_llm::executor::DynamicBatchConfig") const &dynamicBatchConfig*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK18DynamicBatchConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize( : *[DynamicBatchConfig](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfigE "tensorrt_llm::executor::DynamicBatchConfig") const &dynamicBatchConfig*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK18DynamicBatchConfig "Link to this definition")

            static [SchedulerConfig](#_CPPv4N12tensorrt_llm8executor15SchedulerConfigE "tensorrt_llm::executor::SchedulerConfig") deserializeSchedulerConfig(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization26deserializeSchedulerConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[SchedulerConfig](#_CPPv4N12tensorrt_llm8executor15SchedulerConfigE "tensorrt_llm::executor::SchedulerConfig") const &schedulerConfig*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK15SchedulerConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[SchedulerConfig](#_CPPv4N12tensorrt_llm8executor15SchedulerConfigE "tensorrt_llm::executor::SchedulerConfig") const &schedulerConfig*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK15SchedulerConfig "Link to this definition")

            static [ExtendedRuntimePerfKnobConfig](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfigE "tensorrt_llm::executor::ExtendedRuntimePerfKnobConfig") deserializeExtendedRuntimePerfKnobConfig( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization40deserializeExtendedRuntimePerfKnobConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[ExtendedRuntimePerfKnobConfig](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfigE "tensorrt_llm::executor::ExtendedRuntimePerfKnobConfig") const &extendedRuntimePerfKnobConfig*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK29ExtendedRuntimePerfKnobConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize( : *[ExtendedRuntimePerfKnobConfig](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfigE "tensorrt_llm::executor::ExtendedRuntimePerfKnobConfig") const &extendedRuntimePerfKnobConfig*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK29ExtendedRuntimePerfKnobConfig "Link to this definition")

            static [ParallelConfig](#_CPPv4N12tensorrt_llm8executor14ParallelConfigE "tensorrt_llm::executor::ParallelConfig") deserializeParallelConfig(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization25deserializeParallelConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[ParallelConfig](#_CPPv4N12tensorrt_llm8executor14ParallelConfigE "tensorrt_llm::executor::ParallelConfig") const &parallelConfig*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK14ParallelConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[ParallelConfig](#_CPPv4N12tensorrt_llm8executor14ParallelConfigE "tensorrt_llm::executor::ParallelConfig") const &parallelConfig*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK14ParallelConfig "Link to this definition")

            static [PeftCacheConfig](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfigE "tensorrt_llm::executor::PeftCacheConfig") deserializePeftCacheConfig(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization26deserializePeftCacheConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[PeftCacheConfig](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfigE "tensorrt_llm::executor::PeftCacheConfig") const &peftCacheConfig*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK15PeftCacheConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[PeftCacheConfig](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfigE "tensorrt_llm::executor::PeftCacheConfig") const &peftCacheConfig*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK15PeftCacheConfig "Link to this definition")

            static [OrchestratorConfig](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfigE "tensorrt_llm::executor::OrchestratorConfig") deserializeOrchestratorConfig( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization29deserializeOrchestratorConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[OrchestratorConfig](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfigE "tensorrt_llm::executor::OrchestratorConfig") const &orchestratorConfig*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK18OrchestratorConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize( : *[OrchestratorConfig](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfigE "tensorrt_llm::executor::OrchestratorConfig") const &orchestratorConfig*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK18OrchestratorConfig "Link to this definition")

            static [DecodingMode](#_CPPv4N12tensorrt_llm8executor12DecodingModeE "tensorrt_llm::executor::DecodingMode") deserializeDecodingMode(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization23deserializeDecodingModeERNSt7istreamE "Link to this definition")

            static void serialize( : *[DecodingMode](#_CPPv4N12tensorrt_llm8executor12DecodingModeE "tensorrt_llm::executor::DecodingMode") const &decodingMode*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK12DecodingModeRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[DecodingMode](#_CPPv4N12tensorrt_llm8executor12DecodingModeE "tensorrt_llm::executor::DecodingMode") const &decodingMode*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK12DecodingMode "Link to this definition")

            static [LookaheadDecodingConfig](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfigE "tensorrt_llm::executor::LookaheadDecodingConfig") deserializeLookaheadDecodingConfig( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization34deserializeLookaheadDecodingConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[LookaheadDecodingConfig](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfigE "tensorrt_llm::executor::LookaheadDecodingConfig") const &lookaheadDecodingConfig*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK23LookaheadDecodingConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize( : *[LookaheadDecodingConfig](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfigE "tensorrt_llm::executor::LookaheadDecodingConfig") const &lookaheadDecodingConfig*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK23LookaheadDecodingConfig "Link to this definition")

            static [EagleConfig](#_CPPv4N12tensorrt_llm8executor11EagleConfigE "tensorrt_llm::executor::EagleConfig") deserializeEagleConfig(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization22deserializeEagleConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[EagleConfig](#_CPPv4N12tensorrt_llm8executor11EagleConfigE "tensorrt_llm::executor::EagleConfig") const &eagleConfig*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK11EagleConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[EagleConfig](#_CPPv4N12tensorrt_llm8executor11EagleConfigE "tensorrt_llm::executor::EagleConfig") const &eagleConfig*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK11EagleConfig "Link to this definition")

            static [SpeculativeDecodingConfig](#_CPPv4N12tensorrt_llm8executor25SpeculativeDecodingConfigE "tensorrt_llm::executor::SpeculativeDecodingConfig") deserializeSpeculativeDecodingConfig( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization36deserializeSpeculativeDecodingConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[SpeculativeDecodingConfig](#_CPPv4N12tensorrt_llm8executor25SpeculativeDecodingConfigE "tensorrt_llm::executor::SpeculativeDecodingConfig") const &specDecConfig*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK25SpeculativeDecodingConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize( : *[SpeculativeDecodingConfig](#_CPPv4N12tensorrt_llm8executor25SpeculativeDecodingConfigE "tensorrt_llm::executor::SpeculativeDecodingConfig") const &specDecConfig*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK25SpeculativeDecodingConfig "Link to this definition")

            static [GuidedDecodingConfig](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfigE "tensorrt_llm::executor::GuidedDecodingConfig") deserializeGuidedDecodingConfig( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization31deserializeGuidedDecodingConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[GuidedDecodingConfig](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfigE "tensorrt_llm::executor::GuidedDecodingConfig") const &guidedDecodingConfig*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK20GuidedDecodingConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize( : *[GuidedDecodingConfig](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfigE "tensorrt_llm::executor::GuidedDecodingConfig") const &guidedDecodingConfig*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK20GuidedDecodingConfig "Link to this definition")

            static [GuidedDecodingParams](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParamsE "tensorrt_llm::executor::GuidedDecodingParams") deserializeGuidedDecodingParams( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization31deserializeGuidedDecodingParamsERNSt7istreamE "Link to this definition")

            static void serialize( : *[GuidedDecodingParams](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParamsE "tensorrt_llm::executor::GuidedDecodingParams") const &guidedDecodingParams*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK20GuidedDecodingParamsRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize( : *[GuidedDecodingParams](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParamsE "tensorrt_llm::executor::GuidedDecodingParams") const &guidedDecodingParams*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK20GuidedDecodingParams "Link to this definition")

            static [KvCacheRetentionConfig](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfigE "tensorrt_llm::executor::KvCacheRetentionConfig") deserializeKvCacheRetentionConfig( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization33deserializeKvCacheRetentionConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[KvCacheRetentionConfig](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfigE "tensorrt_llm::executor::KvCacheRetentionConfig") const &kvCacheRetentionConfig*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK22KvCacheRetentionConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize( : *[KvCacheRetentionConfig](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfigE "tensorrt_llm::executor::KvCacheRetentionConfig") const &kvCacheRetentionConfig*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK22KvCacheRetentionConfig "Link to this definition")

            static [KvCacheRetentionConfig](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfigE "tensorrt_llm::executor::KvCacheRetentionConfig")::[TokenRangeRetentionConfig](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfigE "tensorrt_llm::executor::KvCacheRetentionConfig::TokenRangeRetentionConfig") deserializeTokenRangeRetentionConfig( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization36deserializeTokenRangeRetentionConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[KvCacheRetentionConfig](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfigE "tensorrt_llm::executor::KvCacheRetentionConfig")::[TokenRangeRetentionConfig](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfigE "tensorrt_llm::executor::KvCacheRetentionConfig::TokenRangeRetentionConfig") const &tokenRangeRetentionConfig*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKN22KvCacheRetentionConfig25TokenRangeRetentionConfigERNSt7ostreamE "Link to this definition")

            static size\_t serializedSize( : *[KvCacheRetentionConfig](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfigE "tensorrt_llm::executor::KvCacheRetentionConfig")::[TokenRangeRetentionConfig](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfigE "tensorrt_llm::executor::KvCacheRetentionConfig::TokenRangeRetentionConfig") const &tokenRangeRetentionConfig*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERKN22KvCacheRetentionConfig25TokenRangeRetentionConfigE "Link to this definition")

            static [DecodingConfig](#_CPPv4N12tensorrt_llm8executor14DecodingConfigE "tensorrt_llm::executor::DecodingConfig") deserializeDecodingConfig(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization25deserializeDecodingConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[DecodingConfig](#_CPPv4N12tensorrt_llm8executor14DecodingConfigE "tensorrt_llm::executor::DecodingConfig") const &decodingConfig*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK14DecodingConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[DecodingConfig](#_CPPv4N12tensorrt_llm8executor14DecodingConfigE "tensorrt_llm::executor::DecodingConfig") const &decodingConfig*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK14DecodingConfig "Link to this definition")

            static [DebugConfig](#_CPPv4N12tensorrt_llm8executor11DebugConfigE "tensorrt_llm::executor::DebugConfig") deserializeDebugConfig(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization22deserializeDebugConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[DebugConfig](#_CPPv4N12tensorrt_llm8executor11DebugConfigE "tensorrt_llm::executor::DebugConfig") const &debugConfig*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK11DebugConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[DebugConfig](#_CPPv4N12tensorrt_llm8executor11DebugConfigE "tensorrt_llm::executor::DebugConfig") const &debugConfig*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK11DebugConfig "Link to this definition")

            static [CacheTransceiverConfig](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfigE "tensorrt_llm::executor::CacheTransceiverConfig") deserializeCacheTransceiverConfig( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization33deserializeCacheTransceiverConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[CacheTransceiverConfig](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfigE "tensorrt_llm::executor::CacheTransceiverConfig") const &cacheTransceiverConfig*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK22CacheTransceiverConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize( : *[CacheTransceiverConfig](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfigE "tensorrt_llm::executor::CacheTransceiverConfig") const &cacheTransceiverConfig*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK22CacheTransceiverConfig "Link to this definition")

            static [ExecutorConfig](#_CPPv4N12tensorrt_llm8executor14ExecutorConfigE "tensorrt_llm::executor::ExecutorConfig") deserializeExecutorConfig(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization25deserializeExecutorConfigERNSt7istreamE "Link to this definition")

            static void serialize( : *[ExecutorConfig](#_CPPv4N12tensorrt_llm8executor14ExecutorConfigE "tensorrt_llm::executor::ExecutorConfig") const &executorConfig*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK14ExecutorConfigRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[ExecutorConfig](#_CPPv4N12tensorrt_llm8executor14ExecutorConfigE "tensorrt_llm::executor::ExecutorConfig") const &executorConfig*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK14ExecutorConfig "Link to this definition")

            static [KvCacheStats](#_CPPv4N12tensorrt_llm8executor12KvCacheStatsE "tensorrt_llm::executor::KvCacheStats") deserializeKvCacheStats(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization23deserializeKvCacheStatsERNSt7istreamE "Link to this definition")

            static void serialize( : *[KvCacheStats](#_CPPv4N12tensorrt_llm8executor12KvCacheStatsE "tensorrt_llm::executor::KvCacheStats") const &kvCacheStats*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK12KvCacheStatsRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[KvCacheStats](#_CPPv4N12tensorrt_llm8executor12KvCacheStatsE "tensorrt_llm::executor::KvCacheStats") const &kvCacheStats*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK12KvCacheStats "Link to this definition")

            static [StaticBatchingStats](#_CPPv4N12tensorrt_llm8executor19StaticBatchingStatsE "tensorrt_llm::executor::StaticBatchingStats") deserializeStaticBatchingStats( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization30deserializeStaticBatchingStatsERNSt7istreamE "Link to this definition")

            static void serialize( : *[StaticBatchingStats](#_CPPv4N12tensorrt_llm8executor19StaticBatchingStatsE "tensorrt_llm::executor::StaticBatchingStats") const &staticBatchingStats*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK19StaticBatchingStatsRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize( : *[StaticBatchingStats](#_CPPv4N12tensorrt_llm8executor19StaticBatchingStatsE "tensorrt_llm::executor::StaticBatchingStats") const &staticBatchingStats*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK19StaticBatchingStats "Link to this definition")

            static [InflightBatchingStats](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStatsE "tensorrt_llm::executor::InflightBatchingStats") deserializeInflightBatchingStats( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization32deserializeInflightBatchingStatsERNSt7istreamE "Link to this definition")

            static void serialize( : *[InflightBatchingStats](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStatsE "tensorrt_llm::executor::InflightBatchingStats") const &inflightBatchingStats*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK21InflightBatchingStatsRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize( : *[InflightBatchingStats](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStatsE "tensorrt_llm::executor::InflightBatchingStats") const &inflightBatchingStats*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK21InflightBatchingStats "Link to this definition")

            static [SpecDecodingStats](#_CPPv4N12tensorrt_llm8executor17SpecDecodingStatsE "tensorrt_llm::executor::SpecDecodingStats") deserializeSpecDecodingStats( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization28deserializeSpecDecodingStatsERNSt7istreamE "Link to this definition")

            static void serialize( : *[SpecDecodingStats](#_CPPv4N12tensorrt_llm8executor17SpecDecodingStatsE "tensorrt_llm::executor::SpecDecodingStats") const &specDecodingStats*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK17SpecDecodingStatsRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize( : *[SpecDecodingStats](#_CPPv4N12tensorrt_llm8executor17SpecDecodingStatsE "tensorrt_llm::executor::SpecDecodingStats") const &specDecodingStats*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK17SpecDecodingStats "Link to this definition")

            static [IterationStats](#_CPPv4N12tensorrt_llm8executor14IterationStatsE "tensorrt_llm::executor::IterationStats") deserializeIterationStats( : *std::vector<char> &buffer*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization25deserializeIterationStatsERNSt6vectorIcEE "Link to this definition")

            static [IterationStats](#_CPPv4N12tensorrt_llm8executor14IterationStatsE "tensorrt_llm::executor::IterationStats") deserializeIterationStats(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization25deserializeIterationStatsERNSt7istreamE "Link to this definition")

            static void serialize( : *[IterationStats](#_CPPv4N12tensorrt_llm8executor14IterationStatsE "tensorrt_llm::executor::IterationStats") const &iterStats*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK14IterationStatsRNSt7ostreamE "Link to this definition")

            static std::vector<char> serialize(*[IterationStats](#_CPPv4N12tensorrt_llm8executor14IterationStatsE "tensorrt_llm::executor::IterationStats") const &iterStats*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK14IterationStats "Link to this definition")

            static size\_t serializedSize(*[IterationStats](#_CPPv4N12tensorrt_llm8executor14IterationStatsE "tensorrt_llm::executor::IterationStats") const &iterStats*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK14IterationStats "Link to this definition")

            static std::vector<char> serialize( : *std::vector<[IterationStats](#_CPPv4N12tensorrt_llm8executor14IterationStatsE "tensorrt_llm::executor::IterationStats")> const &iterStatsVec*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKNSt6vectorI14IterationStatsEE "Link to this definition")

            static std::vector<[IterationStats](#_CPPv4N12tensorrt_llm8executor14IterationStatsE "tensorrt_llm::executor::IterationStats")> deserializeIterationStatsVec( : *std::vector<char> &buffer*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization28deserializeIterationStatsVecERNSt6vectorIcEE "Link to this definition")

            static [DisServingRequestStats](#_CPPv4N12tensorrt_llm8executor22DisServingRequestStatsE "tensorrt_llm::executor::DisServingRequestStats") deserializeDisServingRequestStats( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization33deserializeDisServingRequestStatsERNSt7istreamE "Link to this definition")

            static void serialize( : *[DisServingRequestStats](#_CPPv4N12tensorrt_llm8executor22DisServingRequestStatsE "tensorrt_llm::executor::DisServingRequestStats") const &stats*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK22DisServingRequestStatsRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize( : *[DisServingRequestStats](#_CPPv4N12tensorrt_llm8executor22DisServingRequestStatsE "tensorrt_llm::executor::DisServingRequestStats") const &disServingRequestStats*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK22DisServingRequestStats "Link to this definition")

            static [RequestStage](#_CPPv4N12tensorrt_llm8executor12RequestStageE "tensorrt_llm::executor::RequestStage") deserializeRequestStage(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization23deserializeRequestStageERNSt7istreamE "Link to this definition")

            static void serialize( : *[RequestStage](#_CPPv4N12tensorrt_llm8executor12RequestStageE "tensorrt_llm::executor::RequestStage") const &requestStage*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK12RequestStageRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[RequestStage](#_CPPv4N12tensorrt_llm8executor12RequestStageE "tensorrt_llm::executor::RequestStage") const &requestStage*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK12RequestStage "Link to this definition")

            static [RequestStats](#_CPPv4N12tensorrt_llm8executor12RequestStatsE "tensorrt_llm::executor::RequestStats") deserializeRequestStats(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization23deserializeRequestStatsERNSt7istreamE "Link to this definition")

            static void serialize(*[RequestStats](#_CPPv4N12tensorrt_llm8executor12RequestStatsE "tensorrt_llm::executor::RequestStats") const &state*, *std::ostream &os*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK12RequestStatsRNSt7ostreamE "Link to this definition")

            static size\_t serializedSize(*[RequestStats](#_CPPv4N12tensorrt_llm8executor12RequestStatsE "tensorrt_llm::executor::RequestStats") const &state*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK12RequestStats "Link to this definition")

            static [RequestStatsPerIteration](#_CPPv4N12tensorrt_llm8executor24RequestStatsPerIterationE "tensorrt_llm::executor::RequestStatsPerIteration") deserializeRequestStatsPerIteration( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization35deserializeRequestStatsPerIterationERNSt7istreamE "Link to this definition")

            static [RequestStatsPerIteration](#_CPPv4N12tensorrt_llm8executor24RequestStatsPerIterationE "tensorrt_llm::executor::RequestStatsPerIteration") deserializeRequestStatsPerIteration( : *std::vector<char> &buffer*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization35deserializeRequestStatsPerIterationERNSt6vectorIcEE "Link to this definition")

            static void serialize( : *[RequestStatsPerIteration](#_CPPv4N12tensorrt_llm8executor24RequestStatsPerIterationE "tensorrt_llm::executor::RequestStatsPerIteration") const &state*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK24RequestStatsPerIterationRNSt7ostreamE "Link to this definition")

            static std::vector<char> serialize( : *[RequestStatsPerIteration](#_CPPv4N12tensorrt_llm8executor24RequestStatsPerIterationE "tensorrt_llm::executor::RequestStatsPerIteration") const &state*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK24RequestStatsPerIteration "Link to this definition")

            static size\_t serializedSize(*[RequestStatsPerIteration](#_CPPv4N12tensorrt_llm8executor24RequestStatsPerIterationE "tensorrt_llm::executor::RequestStatsPerIteration") const &state*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK24RequestStatsPerIteration "Link to this definition")

            static std::vector<char> serialize( : *std::vector<[RequestStatsPerIteration](#_CPPv4N12tensorrt_llm8executor24RequestStatsPerIterationE "tensorrt_llm::executor::RequestStatsPerIteration")> const &requestStatsVec*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKNSt6vectorI24RequestStatsPerIterationEE "Link to this definition")

            static std::vector<[RequestStatsPerIteration](#_CPPv4N12tensorrt_llm8executor24RequestStatsPerIterationE "tensorrt_llm::executor::RequestStatsPerIteration")> deserializeRequestStatsPerIterationVec( : *std::vector<char> &buffer*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization38deserializeRequestStatsPerIterationVecERNSt6vectorIcEE "Link to this definition")

            static std::vector<char> serialize( : *std::deque<[KVCacheEvent](#_CPPv4N12tensorrt_llm8executor12KVCacheEventE "tensorrt_llm::executor::KVCacheEvent")> const &kvCacheEvents*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKNSt5dequeI12KVCacheEventEE "Link to this definition")

            static std::deque<[KVCacheEvent](#_CPPv4N12tensorrt_llm8executor12KVCacheEventE "tensorrt_llm::executor::KVCacheEvent")> deserializeKVCacheEvents( : *std::vector<char> &buffer*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization24deserializeKVCacheEventsERNSt6vectorIcEE "Link to this definition")

            static size\_t serializedSize(*[KVCacheEvent](#_CPPv4N12tensorrt_llm8executor12KVCacheEventE "tensorrt_llm::executor::KVCacheEvent") const &event*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK12KVCacheEvent "Link to this definition")

            static void serialize(*[KVCacheEvent](#_CPPv4N12tensorrt_llm8executor12KVCacheEventE "tensorrt_llm::executor::KVCacheEvent") const &event*, *std::ostream &os*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK12KVCacheEventRNSt7ostreamE "Link to this definition")

            static [KVCacheEvent](#_CPPv4N12tensorrt_llm8executor12KVCacheEventE "tensorrt_llm::executor::KVCacheEvent") deserializeKVCacheEvent(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization23deserializeKVCacheEventERNSt7istreamE "Link to this definition")

            static size\_t serializedSize(*[KVCacheCreatedData](#_CPPv4N12tensorrt_llm8executor18KVCacheCreatedDataE "tensorrt_llm::executor::KVCacheCreatedData") const &data*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK18KVCacheCreatedData "Link to this definition")

            static void serialize( : *[KVCacheCreatedData](#_CPPv4N12tensorrt_llm8executor18KVCacheCreatedDataE "tensorrt_llm::executor::KVCacheCreatedData") const &data*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK18KVCacheCreatedDataRNSt7ostreamE "Link to this definition")

            static [KVCacheCreatedData](#_CPPv4N12tensorrt_llm8executor18KVCacheCreatedDataE "tensorrt_llm::executor::KVCacheCreatedData") deserializeKVCacheCreatedData( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization29deserializeKVCacheCreatedDataERNSt7istreamE "Link to this definition")

            static size\_t serializedSize(*[KVCacheStoredData](#_CPPv4N12tensorrt_llm8executor17KVCacheStoredDataE "tensorrt_llm::executor::KVCacheStoredData") const &data*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK17KVCacheStoredData "Link to this definition")

            static void serialize( : *[KVCacheStoredData](#_CPPv4N12tensorrt_llm8executor17KVCacheStoredDataE "tensorrt_llm::executor::KVCacheStoredData") const &data*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK17KVCacheStoredDataRNSt7ostreamE "Link to this definition")

            static [KVCacheStoredData](#_CPPv4N12tensorrt_llm8executor17KVCacheStoredDataE "tensorrt_llm::executor::KVCacheStoredData") deserializeKVCacheStoredData( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization28deserializeKVCacheStoredDataERNSt7istreamE "Link to this definition")

            static size\_t serializedSize(*[KVCacheStoredBlockData](#_CPPv4N12tensorrt_llm8executor22KVCacheStoredBlockDataE "tensorrt_llm::executor::KVCacheStoredBlockData") const &data*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK22KVCacheStoredBlockData "Link to this definition")

            static void serialize( : *[KVCacheStoredBlockData](#_CPPv4N12tensorrt_llm8executor22KVCacheStoredBlockDataE "tensorrt_llm::executor::KVCacheStoredBlockData") const &data*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK22KVCacheStoredBlockDataRNSt7ostreamE "Link to this definition")

            static [KVCacheStoredBlockData](#_CPPv4N12tensorrt_llm8executor22KVCacheStoredBlockDataE "tensorrt_llm::executor::KVCacheStoredBlockData") deserializeKVCacheStoredBlockData( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization33deserializeKVCacheStoredBlockDataERNSt7istreamE "Link to this definition")

            static size\_t serializedSize(*[KVCacheRemovedData](#_CPPv4N12tensorrt_llm8executor18KVCacheRemovedDataE "tensorrt_llm::executor::KVCacheRemovedData") const &data*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK18KVCacheRemovedData "Link to this definition")

            static void serialize( : *[KVCacheRemovedData](#_CPPv4N12tensorrt_llm8executor18KVCacheRemovedDataE "tensorrt_llm::executor::KVCacheRemovedData") const &data*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK18KVCacheRemovedDataRNSt7ostreamE "Link to this definition")

            static [KVCacheRemovedData](#_CPPv4N12tensorrt_llm8executor18KVCacheRemovedDataE "tensorrt_llm::executor::KVCacheRemovedData") deserializeKVCacheRemovedData( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization29deserializeKVCacheRemovedDataERNSt7istreamE "Link to this definition")

            template<typename T> static size\_t serializedSize( : *[KVCacheEventDiff](#_CPPv4I0EN12tensorrt_llm8executor16KVCacheEventDiffE "tensorrt_llm::executor::KVCacheEventDiff")<[T](#_CPPv4I0EN12tensorrt_llm8executor13Serialization14serializedSizeE6size_tRK16KVCacheEventDiffI1TE "tensorrt_llm::executor::Serialization::serializedSize::T")> const &data*, )[#](#_CPPv4I0EN12tensorrt_llm8executor13Serialization14serializedSizeE6size_tRK16KVCacheEventDiffI1TE "Link to this definition")

            template<typename T> static void serialize( : *[KVCacheEventDiff](#_CPPv4I0EN12tensorrt_llm8executor16KVCacheEventDiffE "tensorrt_llm::executor::KVCacheEventDiff")<[T](#_CPPv4I0EN12tensorrt_llm8executor13Serialization9serializeEvRK16KVCacheEventDiffI1TERNSt7ostreamE "tensorrt_llm::executor::Serialization::serialize::T")> const &data*, : *std::ostream &os*, )[#](#_CPPv4I0EN12tensorrt_llm8executor13Serialization9serializeEvRK16KVCacheEventDiffI1TERNSt7ostreamE "Link to this definition")

            template<typename T> static [KVCacheEventDiff](#_CPPv4I0EN12tensorrt_llm8executor16KVCacheEventDiffE "tensorrt_llm::executor::KVCacheEventDiff")<[T](#_CPPv4I0EN12tensorrt_llm8executor13Serialization27deserializeKVCacheEventDiffE16KVCacheEventDiffI1TERNSt7istreamE "tensorrt_llm::executor::Serialization::deserializeKVCacheEventDiff::T")> deserializeKVCacheEventDiff( : *std::istream &is*, )[#](#_CPPv4I0EN12tensorrt_llm8executor13Serialization27deserializeKVCacheEventDiffE16KVCacheEventDiffI1TERNSt7istreamE "Link to this definition")

            static size\_t serializedSize(*[KVCacheUpdatedData](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedDataE "tensorrt_llm::executor::KVCacheUpdatedData") const &data*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK18KVCacheUpdatedData "Link to this definition")

            static void serialize( : *[KVCacheUpdatedData](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedDataE "tensorrt_llm::executor::KVCacheUpdatedData") const &data*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK18KVCacheUpdatedDataRNSt7ostreamE "Link to this definition")

            static [KVCacheUpdatedData](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedDataE "tensorrt_llm::executor::KVCacheUpdatedData") deserializeKVCacheUpdatedData( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization29deserializeKVCacheUpdatedDataERNSt7istreamE "Link to this definition")

            static size\_t serializedSize( : *[tensorrt\_llm](#_CPPv412tensorrt_llm "tensorrt_llm")::[runtime](#_CPPv4N12tensorrt_llm7runtimeE "tensorrt_llm::runtime")::[UniqueToken](runtime.md#_CPPv4N12tensorrt_llm7runtime11UniqueTokenE "tensorrt_llm::runtime::UniqueToken") const &token*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERKN12tensorrt_llm7runtime11UniqueTokenE "Link to this definition")

            static void serialize( : *[tensorrt\_llm](#_CPPv412tensorrt_llm "tensorrt_llm")::[runtime](#_CPPv4N12tensorrt_llm7runtimeE "tensorrt_llm::runtime")::[UniqueToken](runtime.md#_CPPv4N12tensorrt_llm7runtime11UniqueTokenE "tensorrt_llm::runtime::UniqueToken") const &token*, : *std::ostream &os*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKN12tensorrt_llm7runtime11UniqueTokenERNSt7ostreamE "Link to this definition")

            static [tensorrt\_llm](#_CPPv412tensorrt_llm "tensorrt_llm")::[runtime](#_CPPv4N12tensorrt_llm7runtimeE "tensorrt_llm::runtime")::[UniqueToken](runtime.md#_CPPv4N12tensorrt_llm7runtime11UniqueTokenE "tensorrt_llm::runtime::UniqueToken") deserializeUniqueToken( : *std::istream &is*, )[#](#_CPPv4N12tensorrt_llm8executor13Serialization22deserializeUniqueTokenERNSt7istreamE "Link to this definition")

            static std::string deserializeString(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization17deserializeStringERNSt7istreamE "Link to this definition")

            static bool deserializeBool(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization15deserializeBoolERNSt7istreamE "Link to this definition")

            static [ModelType](#_CPPv4N12tensorrt_llm8executor9ModelTypeE "tensorrt_llm::executor::ModelType") deserializeModelType(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor13Serialization20deserializeModelTypeERNSt7istreamE "Link to this definition")

        namespace kv\_cache

## disaggServerUtil.h[#](#disaggserverutil-h "Link to this heading")

namespace tensorrt\_llm
:   namespace executor
    :   namespace disagg\_executor[#](#_CPPv4N12tensorrt_llm8executor15disagg_executorE "Link to this definition")
        :   class DisaggExecutorOrchestrator[#](#_CPPv4N12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestratorE "Link to this definition")
            :   Public Functions

                DisaggExecutorOrchestrator( : *std::vector<std::filesystem::path> const &ctxEnginePaths*, : *std::vector<std::filesystem::path> const &genEnginePaths*, : *std::vector<[executor](#_CPPv4N12tensorrt_llm8executorE "tensorrt_llm::executor")::[ExecutorConfig](#_CPPv4N12tensorrt_llm8executor14ExecutorConfigE "tensorrt_llm::executor::ExecutorConfig")> const &ctxExecutorConfigs*, : *std::vector<[executor](#_CPPv4N12tensorrt_llm8executorE "tensorrt_llm::executor")::[ExecutorConfig](#_CPPv4N12tensorrt_llm8executor14ExecutorConfigE "tensorrt_llm::executor::ExecutorConfig")> const &genExecutorConfigs*, : *bool hasContextAwaitThreads*, : *bool hasGenAwaitThreads*, )[#](#_CPPv4N12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestrator26DisaggExecutorOrchestratorERKNSt6vectorINSt10filesystem4pathEEERKNSt6vectorINSt10filesystem4pathEEERKNSt6vectorIN8executor14ExecutorConfigEEERKNSt6vectorIN8executor14ExecutorConfigEEEbb "Link to this definition")
                :   Constructs a [DisaggExecutorOrchestrator](#classtensorrt__llm_1_1executor_1_1disagg__executor_1_1DisaggExecutorOrchestrator) object.

                    Parameters:
                    :   * **ctxEnginePaths** – A vector of file paths to context engine files.
                        * **genEnginePaths** – A vector of file paths to generation engine files.
                        * **ctxExecutorConfigs** – A vector of [ExecutorConfig](#classtensorrt__llm_1_1executor_1_1ExecutorConfig) for context executors.
                        * **genExecutorConfigs** – A vector of [ExecutorConfig](#classtensorrt__llm_1_1executor_1_1ExecutorConfig) for generation executors.
                        * **hasContextAwaitThreads** – Whether or not there are threads that receive response for each generation executor.
                        * **hasGenAwaitThreads** – Whether or not there are threads that receive response for each generation executor.

                std::vector<[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType")> enqueueContext( : *std::vector<texec::Request> const &requests*, : *std::optional<int> selectContextId = std::nullopt*, : *bool batch = false*, )[#](#_CPPv4N12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestrator14enqueueContextERKNSt6vectorIN5texec7RequestEEENSt8optionalIiEEb "Link to this definition")
                :   Enqueue context-only requests to context executors.

                    Parameters:
                    :   * **requests** – A vector of context-only requests.
                        * **selectContextId** – The index of the context executor to use. If `std::nullopt`, the executor that has the smallest number of inflight requests will be used.
                        * **batch** – If true,enqueue requests in same context executor.If false, will try to use a different executor for each request.

                    Returns:
                    :   A vector of global request ids, corresponding to the order of the requests in `requests`, the id returned may be different from the request id in each executor.

                void enqueueGeneration( : *std::vector<texec::Request> const &requests*, : *std::vector<[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType")> const &globalRequestIds*, : *std::optional<int> selectGenIdx = std::nullopt*, : *bool batch = false*, )[#](#_CPPv4N12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestrator17enqueueGenerationERKNSt6vectorIN5texec7RequestEEERKNSt6vectorI6IdTypeEENSt8optionalIiEEb "Link to this definition")
                :   Enqueue generation-only requests to generation executors.

                    Parameters:
                    :   * **requests** – A vector of generation-only requests.
                        * **globalRequestIds** – A vector of global request ids, corresponding to the order of the requests,and must be the ids returned by the enqueueContext function.
                        * **selectGenIdx** – The index of the generation executor to use. If `std::nullopt`, the executor that has the smallest number of inflight requests will be used.
                        * **batch** – If true,enqueue requests in same generation executor.If false, will try to use a different executor for each request.

                std::vector<[ResponseWithId](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithIdE "tensorrt_llm::executor::disagg_executor::ResponseWithId")> awaitContextResponses( : *std::optional<std::chrono::milliseconds> const &timeout*, : *std::optional<int> contextIdx = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestrator21awaitContextResponsesERKNSt8optionalINSt6chrono12millisecondsEEENSt8optionalIiEE "Link to this definition")
                :   Await for context responses.

                    Parameters:
                    :   * **timeout** – The maximum time to wait for new responses
                        * **contextIdx** – The index of the context executor to use. If `std::nullopt`, return ready responses in all context executors,if `hasContextAwaitThreads` is true, then this parameter must be std::nullopt.

                    Returns:
                    :   A vector of responses with corresponding global request ids

                std::vector<[ResponseWithId](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithIdE "tensorrt_llm::executor::disagg_executor::ResponseWithId")> awaitGenerationResponses( : *std::optional<std::chrono::milliseconds> const &timeout*, : *std::optional<int> genIdx = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestrator24awaitGenerationResponsesERKNSt8optionalINSt6chrono12millisecondsEEENSt8optionalIiEE "Link to this definition")
                :   Await for generation responses.

                    Parameters:
                    :   * **timeout** – The maximum time to wait for new responses.
                        * **genIdx** – The index of the generation executor to use. If `std::nullopt`, return ready responses in all generation executors,if `hasGenAwaitThreads` is true, then this parameter must be std::nullopt.

                    Returns:
                    :   A vector of responses with corresponding global request ids.

                bool canEnqueue() const[#](#_CPPv4NK12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestrator10canEnqueueEv "Link to this definition")
                :   Indicates if the current process is allowed to enqueueRequests.

                std::vector<std::unique\_ptr<texec::Executor>> const &getContextExecutors() const[#](#_CPPv4NK12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestrator19getContextExecutorsEv "Link to this definition")
                :   Get context executors.

                std::vector<std::unique\_ptr<texec::Executor>> const &getGenExecutors() const[#](#_CPPv4NK12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestrator15getGenExecutorsEv "Link to this definition")
                :   Get generation executors.

                ~DisaggExecutorOrchestrator()[#](#_CPPv4N12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestratorD0Ev "Link to this definition")

                Private Members

                std::unique\_ptr<Impl> mImpl[#](#_CPPv4N12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestrator5mImplE "Link to this definition")

            struct ResponseWithId[#](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithIdE "Link to this definition")
            :   Public Functions

                inline ResponseWithId( : *[tensorrt\_llm](#_CPPv412tensorrt_llm "tensorrt_llm")::[executor](#_CPPv4N12tensorrt_llm8executorE "tensorrt_llm::executor")::[Response](#_CPPv4N12tensorrt_llm8executor8ResponseE "tensorrt_llm::executor::Response") &&response*, : *[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") gid*, )[#](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithId14ResponseWithIdERRN12tensorrt_llm8executor8ResponseE6IdType "Link to this definition")

                inline ResponseWithId( : *[tensorrt\_llm](#_CPPv412tensorrt_llm "tensorrt_llm")::[executor](#_CPPv4N12tensorrt_llm8executorE "tensorrt_llm::executor")::[Response](#_CPPv4N12tensorrt_llm8executor8ResponseE "tensorrt_llm::executor::Response") const &response*, : *[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") gid*, )[#](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithId14ResponseWithIdERKN12tensorrt_llm8executor8ResponseE6IdType "Link to this definition")

                inline ResponseWithId(*[ResponseWithId](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithId14ResponseWithIdERR14ResponseWithId "tensorrt_llm::executor::disagg_executor::ResponseWithId::ResponseWithId") &&other*) noexcept[#](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithId14ResponseWithIdERR14ResponseWithId "Link to this definition")

                ResponseWithId(*[ResponseWithId](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithId14ResponseWithIdERK14ResponseWithId "tensorrt_llm::executor::disagg_executor::ResponseWithId::ResponseWithId") const &other*) = default[#](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithId14ResponseWithIdERK14ResponseWithId "Link to this definition")

                inline [ResponseWithId](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithIdE "tensorrt_llm::executor::disagg_executor::ResponseWithId") &operator=(*[ResponseWithId](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithIdE "tensorrt_llm::executor::disagg_executor::ResponseWithId") &&other*) noexcept[#](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithIdaSERR14ResponseWithId "Link to this definition")

                inline [ResponseWithId](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithIdE "tensorrt_llm::executor::disagg_executor::ResponseWithId") &operator=(*[ResponseWithId](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithIdE "tensorrt_llm::executor::disagg_executor::ResponseWithId") const &other*)[#](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithIdaSERK14ResponseWithId "Link to this definition")

                ~ResponseWithId() = default[#](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithIdD0Ev "Link to this definition")

                Public Members

                [tensorrt\_llm](#_CPPv412tensorrt_llm "tensorrt_llm")::[executor](#_CPPv4N12tensorrt_llm8executorE "tensorrt_llm::executor")::[Response](#_CPPv4N12tensorrt_llm8executor8ResponseE "tensorrt_llm::executor::Response") response[#](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithId8responseE "Link to this definition")

                [IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") gid[#](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithId3gidE "Link to this definition")

## dataTransceiverState.h[#](#datatransceiverstate-h "Link to this heading")

namespace tensorrt\_llm
:   namespace executor
    :   class DataTransceiverState[#](#_CPPv4N12tensorrt_llm8executor20DataTransceiverStateE "Link to this definition")
        :   Public Functions

            DataTransceiverState() = default[#](#_CPPv4N12tensorrt_llm8executor20DataTransceiverState20DataTransceiverStateEv "Link to this definition")

            inline DataTransceiverState( : *[kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[CacheState](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheStateE "tensorrt_llm::executor::kv_cache::CacheState") cacheState*, : *[kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[CommState](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommStateE "tensorrt_llm::executor::kv_cache::CommState") commState*, )[#](#_CPPv4N12tensorrt_llm8executor20DataTransceiverState20DataTransceiverStateEN8kv_cache10CacheStateEN8kv_cache9CommStateE "Link to this definition")

            inline void setCacheState(*[kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[CacheState](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheStateE "tensorrt_llm::executor::kv_cache::CacheState") state*)[#](#_CPPv4N12tensorrt_llm8executor20DataTransceiverState13setCacheStateEN8kv_cache10CacheStateE "Link to this definition")

            inline std::optional<[kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[CacheState](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheStateE "tensorrt_llm::executor::kv_cache::CacheState")> const &getCacheState() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor20DataTransceiverState13getCacheStateEv "Link to this definition")

            inline void setCommState(*[kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[CommState](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommStateE "tensorrt_llm::executor::kv_cache::CommState") state*)[#](#_CPPv4N12tensorrt_llm8executor20DataTransceiverState12setCommStateEN8kv_cache9CommStateE "Link to this definition")

            inline std::optional<[kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[CommState](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommStateE "tensorrt_llm::executor::kv_cache::CommState")> const &getCommState() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor20DataTransceiverState12getCommStateEv "Link to this definition")

            inline bool operator==( : *[DataTransceiverState](#_CPPv4N12tensorrt_llm8executor20DataTransceiverStateE "tensorrt_llm::executor::DataTransceiverState") const &other*, ) const noexcept[#](#_CPPv4NK12tensorrt_llm8executor20DataTransceiverStateeqERK20DataTransceiverState "Link to this definition")

            inline std::string toString() const[#](#_CPPv4NK12tensorrt_llm8executor20DataTransceiverState8toStringEv "Link to this definition")

            Private Members

            std::optional<[kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[CacheState](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheStateE "tensorrt_llm::executor::kv_cache::CacheState")> mCacheState[#](#_CPPv4N12tensorrt_llm8executor20DataTransceiverState11mCacheStateE "Link to this definition")

            std::optional<[kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[CommState](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommStateE "tensorrt_llm::executor::kv_cache::CommState")> mCommState[#](#_CPPv4N12tensorrt_llm8executor20DataTransceiverState10mCommStateE "Link to this definition")

            Friends

            *friend class* Serialization

        namespace kv\_cache
        :   struct AgentState[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10AgentStateE "Link to this definition")
            :   Public Functions

                inline AgentState(*std::string agentName*, *std::string connectionInfo*)[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10AgentState10AgentStateENSt6stringENSt6stringE "Link to this definition")

                AgentState() = default[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10AgentState10AgentStateEv "Link to this definition")

                inline bool operator==(*[AgentState](#_CPPv4N12tensorrt_llm8executor8kv_cache10AgentStateE "tensorrt_llm::executor::kv_cache::AgentState") const &other*) const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache10AgentStateeqERK10AgentState "Link to this definition")

                inline std::string toString() const[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache10AgentState8toStringEv "Link to this definition")

                Public Members

                std::string mAgentName[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10AgentState10mAgentNameE "Link to this definition")

                std::string mConnectionInfo[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10AgentState15mConnectionInfoE "Link to this definition")

            class CacheState[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheStateE "Link to this definition")
            :   Public Types

                enum class AttentionType : std::uint8\_t[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState13AttentionTypeE "Link to this definition")
                :   *Values:*

                    enumerator kDEFAULT[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState13AttentionType8kDEFAULTE "Link to this definition")

                    enumerator kMLA[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState13AttentionType4kMLAE "Link to this definition")

                Public Functions

                inline CacheState( : *[ModelConfig](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState11ModelConfigE "tensorrt_llm::executor::kv_cache::CacheState::ModelConfig") modelConfig*, : *[runtime](#_CPPv4N12tensorrt_llm7runtimeE "tensorrt_llm::runtime")::[WorldConfig](runtime.md#_CPPv4N12tensorrt_llm7runtime11WorldConfigE "tensorrt_llm::runtime::WorldConfig") const &worldConfig*, : *std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &attentionLayerNumPerPP*, : *[nvinfer1](runtime.md#_CPPv48nvinfer1 "nvinfer1")::DataType dataType*, : *[AttentionType](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState13AttentionTypeE "tensorrt_llm::executor::kv_cache::CacheState::AttentionType") attentionType = [AttentionType](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState13AttentionTypeE "tensorrt_llm::executor::kv_cache::CacheState::AttentionType")::[kDEFAULT](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState13AttentionType8kDEFAULTE "tensorrt_llm::executor::kv_cache::CacheState::AttentionType::kDEFAULT")*, : *int kvFactor = 2*, )[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState10CacheStateE11ModelConfigRKN7runtime11WorldConfigERKNSt6vectorI10SizeType32EEN8nvinfer18DataTypeE13AttentionTypei "Link to this definition")

                inline CacheState( : *std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> nbKvHeadPerLayer*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") sizePerHead*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") tokensPerBlock*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") tensorParallelism*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") pipelineParallelism*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") contextParallelism*, : *std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &attentionLayerNumPerPP*, : *[nvinfer1](runtime.md#_CPPv48nvinfer1 "nvinfer1")::DataType dataType*, : *[AttentionType](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState13AttentionTypeE "tensorrt_llm::executor::kv_cache::CacheState::AttentionType") attentionType = [AttentionType](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState13AttentionTypeE "tensorrt_llm::executor::kv_cache::CacheState::AttentionType")::[kDEFAULT](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState13AttentionType8kDEFAULTE "tensorrt_llm::executor::kv_cache::CacheState::AttentionType::kDEFAULT")*, : *int kvFactor = 2*, : *bool enableAttentionDP = false*, : *int DPrank = 0*, : *int DPsize = 0*, )[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState10CacheStateENSt6vectorI10SizeType32EE10SizeType3210SizeType3210SizeType3210SizeType3210SizeType32RKNSt6vectorI10SizeType32EEN8nvinfer18DataTypeE13AttentionTypeibii "Link to this definition")

                inline CacheState( : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") nbAttentionLayers*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") nbKvHeads*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") sizePerHead*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") tokensPerBlock*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") tensorParallelism*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") pipelineParallelism*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") contextParallelism*, : *std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &attentionLayerNumPerPP*, : *[nvinfer1](runtime.md#_CPPv48nvinfer1 "nvinfer1")::DataType dataType*, : *[AttentionType](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState13AttentionTypeE "tensorrt_llm::executor::kv_cache::CacheState::AttentionType") attentionType = [AttentionType](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState13AttentionTypeE "tensorrt_llm::executor::kv_cache::CacheState::AttentionType")::[kDEFAULT](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState13AttentionType8kDEFAULTE "tensorrt_llm::executor::kv_cache::CacheState::AttentionType::kDEFAULT")*, : *int kvFactor = 2*, : *bool enableAttentionDP = false*, : *int DPrank = 0*, : *int DPsize = 0*, )[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState10CacheStateE10SizeType3210SizeType3210SizeType3210SizeType3210SizeType3210SizeType3210SizeType32RKNSt6vectorI10SizeType32EEN8nvinfer18DataTypeE13AttentionTypeibii "Link to this definition")

                inline bool operator==( : *[kv\_cache](#_CPPv4N12tensorrt_llm8executor8kv_cacheE "tensorrt_llm::executor::kv_cache")::[CacheState](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheStateE "tensorrt_llm::executor::kv_cache::CacheState") const &other*, ) const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache10CacheStateeqERKN8kv_cache10CacheStateE "Link to this definition")

                inline [ModelConfig](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState11ModelConfigE "tensorrt_llm::executor::kv_cache::CacheState::ModelConfig") const &getModelConfig() const[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache10CacheState14getModelConfigEv "Link to this definition")

                inline [ParallelConfig](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfigE "tensorrt_llm::executor::kv_cache::CacheState::ParallelConfig") const &getParallelConfig() const[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache10CacheState17getParallelConfigEv "Link to this definition")

                inline [AttentionConfig](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState15AttentionConfigE "tensorrt_llm::executor::kv_cache::CacheState::AttentionConfig") const &getAttentionConfig() const[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache10CacheState18getAttentionConfigEv "Link to this definition")

                inline [nvinfer1](runtime.md#_CPPv48nvinfer1 "nvinfer1")::DataType const &getDataType() const[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache10CacheState11getDataTypeEv "Link to this definition")

                inline std::string toString() const[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache10CacheState8toStringEv "Link to this definition")

                Private Members

                [ModelConfig](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState11ModelConfigE "tensorrt_llm::executor::kv_cache::CacheState::ModelConfig") mModelConfig[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState12mModelConfigE "Link to this definition")

                [ParallelConfig](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfigE "tensorrt_llm::executor::kv_cache::CacheState::ParallelConfig") mParallelConfig[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState15mParallelConfigE "Link to this definition")

                [nvinfer1](runtime.md#_CPPv48nvinfer1 "nvinfer1")::DataType mDataType[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState9mDataTypeE "Link to this definition")

                [AttentionConfig](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState15AttentionConfigE "tensorrt_llm::executor::kv_cache::CacheState::AttentionConfig") mAttentionConfig[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState16mAttentionConfigE "Link to this definition")

                Friends

                *friend class* tensorrt\_llm::executor::Serialization

                struct AttentionConfig[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState15AttentionConfigE "Link to this definition")
                :   Public Functions

                    inline AttentionConfig(*[AttentionType](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState13AttentionTypeE "tensorrt_llm::executor::kv_cache::CacheState::AttentionType") attentionType*, *int kvFactor*)[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState15AttentionConfig15AttentionConfigE13AttentionTypei "Link to this definition")

                    inline bool operator==(*[AttentionConfig](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState15AttentionConfigE "tensorrt_llm::executor::kv_cache::CacheState::AttentionConfig") const &other*) const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache10CacheState15AttentionConfigeqERK15AttentionConfig "Link to this definition")

                    Public Members

                    [AttentionType](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState13AttentionTypeE "tensorrt_llm::executor::kv_cache::CacheState::AttentionType") mAttentionType[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState15AttentionConfig14mAttentionTypeE "Link to this definition")

                    int mKvFactor[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState15AttentionConfig9mKvFactorE "Link to this definition")

                struct ModelConfig[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState11ModelConfigE "Link to this definition")
                :   Public Functions

                    inline bool operator==(*[ModelConfig](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState11ModelConfigE "tensorrt_llm::executor::kv_cache::CacheState::ModelConfig") const &other*) const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache10CacheState11ModelConfigeqERK11ModelConfig "Link to this definition")

                    Public Members

                    std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> mNbKvHeadsPerLayer[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState11ModelConfig18mNbKvHeadsPerLayerE "Link to this definition")

                    [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mSizePerHead[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState11ModelConfig12mSizePerHeadE "Link to this definition")

                    [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mTokensPerBlock[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState11ModelConfig15mTokensPerBlockE "Link to this definition")

                struct ParallelConfig[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfigE "Link to this definition")
                :   Public Functions

                    inline bool operator==(*[ParallelConfig](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfigE "tensorrt_llm::executor::kv_cache::CacheState::ParallelConfig") const &other*) const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfigeqERK14ParallelConfig "Link to this definition")

                    Public Members

                    [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mTensorParallelism[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfig18mTensorParallelismE "Link to this definition")

                    [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mPipelineParallelism[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfig20mPipelineParallelismE "Link to this definition")

                    [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mContextParallelism[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfig19mContextParallelismE "Link to this definition")

                    bool mEnableAttentionDP[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfig18mEnableAttentionDPE "Link to this definition")

                    [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mDPrank[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfig7mDPrankE "Link to this definition")

                    [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mDPsize[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfig7mDPsizeE "Link to this definition")

                    std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> mAttentionLayerNumPerPP[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfig23mAttentionLayerNumPerPPE "Link to this definition")

            class CommState[#](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommStateE "Link to this definition")
            :   Public Functions

                CommState() = default[#](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommState9CommStateEv "Link to this definition")

                inline explicit CommState( : *std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> ranks*, : *int selfIdx = -1*, )[#](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommState9CommStateENSt6vectorI10SizeType32EEi "Link to this definition")

                inline explicit CommState( : *std::vector<[SocketState](#_CPPv4N12tensorrt_llm8executor8kv_cache11SocketStateE "tensorrt_llm::executor::kv_cache::SocketState")> socketState*, : *int selfIdx = -1*, )[#](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommState9CommStateENSt6vectorI11SocketStateEEi "Link to this definition")

                inline CommState(*std::uint16\_t port*, *std::string ip*)[#](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommState9CommStateENSt8uint16_tENSt6stringE "Link to this definition")

                inline explicit CommState( : *std::vector<[AgentState](#_CPPv4N12tensorrt_llm8executor8kv_cache10AgentStateE "tensorrt_llm::executor::kv_cache::AgentState")> agentState*, : *int selfIdx = -1*, )[#](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommState9CommStateENSt6vectorI10AgentStateEEi "Link to this definition")

                inline bool isMpiState() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache9CommState10isMpiStateEv "Link to this definition")

                inline bool isSocketState() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache9CommState13isSocketStateEv "Link to this definition")

                inline bool isAgentState() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache9CommState12isAgentStateEv "Link to this definition")

                inline [MpiState](#_CPPv4N12tensorrt_llm8executor8kv_cache8MpiStateE "tensorrt_llm::executor::kv_cache::MpiState") const &getMpiState() const[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache9CommState11getMpiStateEv "Link to this definition")

                inline std::vector<[SocketState](#_CPPv4N12tensorrt_llm8executor8kv_cache11SocketStateE "tensorrt_llm::executor::kv_cache::SocketState")> const &getSocketState() const[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache9CommState14getSocketStateEv "Link to this definition")

                inline std::vector<[AgentState](#_CPPv4N12tensorrt_llm8executor8kv_cache10AgentStateE "tensorrt_llm::executor::kv_cache::AgentState")> const &getAgentState() const[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache9CommState13getAgentStateEv "Link to this definition")

                inline int getSelfIdx() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache9CommState10getSelfIdxEv "Link to this definition")

                inline bool operator==(*[CommState](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommStateE "tensorrt_llm::executor::kv_cache::CommState") const &other*) const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache9CommStateeqERK9CommState "Link to this definition")

                inline std::string toString() const[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache9CommState8toStringEv "Link to this definition")

                Private Members

                std::variant<std::monostate, [MpiState](#_CPPv4N12tensorrt_llm8executor8kv_cache8MpiStateE "tensorrt_llm::executor::kv_cache::MpiState"), std::vector<[SocketState](#_CPPv4N12tensorrt_llm8executor8kv_cache11SocketStateE "tensorrt_llm::executor::kv_cache::SocketState")>, std::vector<[AgentState](#_CPPv4N12tensorrt_llm8executor8kv_cache10AgentStateE "tensorrt_llm::executor::kv_cache::AgentState")>> mState[#](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommState6mStateE "Link to this definition")

                int mSelfIdx = {-1}[#](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommState8mSelfIdxE "Link to this definition")

                Friends

                *friend class* tensorrt\_llm::executor::Serialization

            struct MpiState[#](#_CPPv4N12tensorrt_llm8executor8kv_cache8MpiStateE "Link to this definition")
            :   Public Functions

                inline bool operator==(*[MpiState](#_CPPv4N12tensorrt_llm8executor8kv_cache8MpiStateE "tensorrt_llm::executor::kv_cache::MpiState") const &other*) const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache8MpiStateeqERK8MpiState "Link to this definition")

                inline std::string toString() const[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache8MpiState8toStringEv "Link to this definition")

                Public Members

                std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> mRanks[#](#_CPPv4N12tensorrt_llm8executor8kv_cache8MpiState6mRanksE "Link to this definition")

            struct SocketState[#](#_CPPv4N12tensorrt_llm8executor8kv_cache11SocketStateE "Link to this definition")
            :   Public Functions

                inline bool operator==(*[SocketState](#_CPPv4N12tensorrt_llm8executor8kv_cache11SocketStateE "tensorrt_llm::executor::kv_cache::SocketState") const &other*) const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache11SocketStateeqERK11SocketState "Link to this definition")

                inline std::string toString() const[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache11SocketState8toStringEv "Link to this definition")

                Public Members

                std::uint16\_t mPort[#](#_CPPv4N12tensorrt_llm8executor8kv_cache11SocketState5mPortE "Link to this definition")

                std::string mIp[#](#_CPPv4N12tensorrt_llm8executor8kv_cache11SocketState3mIpE "Link to this definition")

## tensor.h[#](#tensor-h "Link to this heading")

namespace tensorrt\_llm
:   namespace executor
    :   class Shape : public [tensorrt\_llm](#_CPPv412tensorrt_llm "tensorrt_llm")::common::ArrayView<[detail](#_CPPv4N12tensorrt_llm8executor6detailE "tensorrt_llm::executor::detail")::[DimType64](#_CPPv4N12tensorrt_llm8executor6detail9DimType64E "tensorrt_llm::executor::detail::DimType64") const>[#](#_CPPv4N12tensorrt_llm8executor5ShapeE "Link to this definition")
        :   Public Types

            using Base = [tensorrt\_llm](#_CPPv412tensorrt_llm "tensorrt_llm")::common::ArrayView<[detail](#_CPPv4N12tensorrt_llm8executor6detailE "tensorrt_llm::executor::detail")::[DimType64](#_CPPv4N12tensorrt_llm8executor6detail9DimType64E "tensorrt_llm::executor::detail::DimType64") const>[#](#_CPPv4N12tensorrt_llm8executor5Shape4BaseE "Link to this definition")

            using DimType64 = typename std::remove\_cv\_t<[Base](#_CPPv4N12tensorrt_llm8executor5Shape4BaseE "tensorrt_llm::executor::Shape::Base")::value\_type>[#](#_CPPv4N12tensorrt_llm8executor5Shape9DimType64E "Link to this definition")

            Public Functions

            inline Shape()[#](#_CPPv4N12tensorrt_llm8executor5Shape5ShapeEv "Link to this definition")

            inline Shape(*[DimType64](#_CPPv4N12tensorrt_llm8executor5Shape9DimType64E "tensorrt_llm::executor::Shape::DimType64") const \*data*, *[Base](#_CPPv4N12tensorrt_llm8executor5Shape4BaseE "tensorrt_llm::executor::Shape::Base")::size\_type size*)[#](#_CPPv4N12tensorrt_llm8executor5Shape5ShapeEPK9DimType64N4Base9size_typeE "Link to this definition")

            inline Shape(*std::initializer\_list<[DimType64](#_CPPv4N12tensorrt_llm8executor5Shape9DimType64E "tensorrt_llm::executor::Shape::DimType64")> dims*)[#](#_CPPv4N12tensorrt_llm8executor5Shape5ShapeENSt16initializer_listI9DimType64EE "Link to this definition")

        class Tensor[#](#_CPPv4N12tensorrt_llm8executor6TensorE "Link to this definition")
        :   Public Types

            using CudaStreamPtr = std::shared\_ptr<[runtime](#_CPPv4N12tensorrt_llm7runtimeE "tensorrt_llm::runtime")::[CudaStream](runtime.md#_CPPv4N12tensorrt_llm7runtime10CudaStreamE "tensorrt_llm::runtime::CudaStream")>[#](#_CPPv4N12tensorrt_llm8executor6Tensor13CudaStreamPtrE "Link to this definition")

            Public Functions

            [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") copyToCpu(*[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")::[CudaStreamPtr](#_CPPv4N12tensorrt_llm8executor6Tensor13CudaStreamPtrE "tensorrt_llm::executor::Tensor::CudaStreamPtr") stream = nullptr*) const[#](#_CPPv4NK12tensorrt_llm8executor6Tensor9copyToCpuEN6Tensor13CudaStreamPtrE "Link to this definition")

            [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") copyToPinned(*[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")::[CudaStreamPtr](#_CPPv4N12tensorrt_llm8executor6Tensor13CudaStreamPtrE "tensorrt_llm::executor::Tensor::CudaStreamPtr") stream = nullptr*) const[#](#_CPPv4NK12tensorrt_llm8executor6Tensor12copyToPinnedEN6Tensor13CudaStreamPtrE "Link to this definition")

            [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") copyToPooledPinned(*[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")::[CudaStreamPtr](#_CPPv4N12tensorrt_llm8executor6Tensor13CudaStreamPtrE "tensorrt_llm::executor::Tensor::CudaStreamPtr") stream = nullptr*) const[#](#_CPPv4NK12tensorrt_llm8executor6Tensor18copyToPooledPinnedEN6Tensor13CudaStreamPtrE "Link to this definition")

            [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") copyToManaged(*[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")::[CudaStreamPtr](#_CPPv4N12tensorrt_llm8executor6Tensor13CudaStreamPtrE "tensorrt_llm::executor::Tensor::CudaStreamPtr") stream = nullptr*) const[#](#_CPPv4NK12tensorrt_llm8executor6Tensor13copyToManagedEN6Tensor13CudaStreamPtrE "Link to this definition")

            [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") copyToGpu(*[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")::[CudaStreamPtr](#_CPPv4N12tensorrt_llm8executor6Tensor13CudaStreamPtrE "tensorrt_llm::executor::Tensor::CudaStreamPtr") stream*) const[#](#_CPPv4NK12tensorrt_llm8executor6Tensor9copyToGpuEN6Tensor13CudaStreamPtrE "Link to this definition")

            Tensor() noexcept = default[#](#_CPPv4N12tensorrt_llm8executor6Tensor6TensorEv "Link to this definition")

            ~Tensor() = default[#](#_CPPv4N12tensorrt_llm8executor6TensorD0Ev "Link to this definition")

            Tensor(*[Tensor](#_CPPv4N12tensorrt_llm8executor6Tensor6TensorERK6Tensor "tensorrt_llm::executor::Tensor::Tensor") const &other*) noexcept = default[#](#_CPPv4N12tensorrt_llm8executor6Tensor6TensorERK6Tensor "Link to this definition")

            Tensor(*[Tensor](#_CPPv4N12tensorrt_llm8executor6Tensor6TensorERR6Tensor "tensorrt_llm::executor::Tensor::Tensor") &&other*) noexcept = default[#](#_CPPv4N12tensorrt_llm8executor6Tensor6TensorERR6Tensor "Link to this definition")

            [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") &operator=(*[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") const &other*) noexcept = default[#](#_CPPv4N12tensorrt_llm8executor6TensoraSERK6Tensor "Link to this definition")

            [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") &operator=(*[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") &&other*) noexcept = default[#](#_CPPv4N12tensorrt_llm8executor6TensoraSERR6Tensor "Link to this definition")

            void \*getData()[#](#_CPPv4N12tensorrt_llm8executor6Tensor7getDataEv "Link to this definition")
            :   Returns a pointer to underlying array.

            void const \*getData() const[#](#_CPPv4NK12tensorrt_llm8executor6Tensor7getDataEv "Link to this definition")
            :   Returns a pointer to underlying array.

            [DataType](#_CPPv4N12tensorrt_llm8executor8DataTypeE "tensorrt_llm::executor::DataType") getDataType() const[#](#_CPPv4NK12tensorrt_llm8executor6Tensor11getDataTypeEv "Link to this definition")
            :   Returns the data type of the buffer.

            [MemoryType](#_CPPv4N12tensorrt_llm8executor10MemoryTypeE "tensorrt_llm::executor::MemoryType") getMemoryType() const[#](#_CPPv4NK12tensorrt_llm8executor6Tensor13getMemoryTypeEv "Link to this definition")
            :   Returns the memory type of the buffer.

            [Shape](#_CPPv4N12tensorrt_llm8executor5ShapeE "tensorrt_llm::executor::Shape") getShape() const[#](#_CPPv4NK12tensorrt_llm8executor6Tensor8getShapeEv "Link to this definition")
            :   Returns the tensor dimensions.

            std::size\_t getSize() const[#](#_CPPv4NK12tensorrt_llm8executor6Tensor7getSizeEv "Link to this definition")
            :   Returns the number of elements in the tensor.

            std::size\_t getSizeInBytes() const[#](#_CPPv4NK12tensorrt_llm8executor6Tensor14getSizeInBytesEv "Link to this definition")
            :   Returns the size of the tensor in bytes.

            void setZero(*[CudaStreamPtr](#_CPPv4N12tensorrt_llm8executor6Tensor13CudaStreamPtrE "tensorrt_llm::executor::Tensor::CudaStreamPtr") stream = nullptr*)[#](#_CPPv4N12tensorrt_llm8executor6Tensor7setZeroE13CudaStreamPtr "Link to this definition")
            :   Set the entire memory to zero.

                Parameters:
                :   **stream** – Must be a valid CUDA stream if the memory type is GPU.

            void setFrom(*[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") const &other*, *[CudaStreamPtr](#_CPPv4N12tensorrt_llm8executor6Tensor13CudaStreamPtrE "tensorrt_llm::executor::Tensor::CudaStreamPtr") stream = nullptr*)[#](#_CPPv4N12tensorrt_llm8executor6Tensor7setFromERK6Tensor13CudaStreamPtr "Link to this definition")
            :   Copy the data and shape from another tensor.

                Parameters:
                :   * **other** – A tensor to copy from.
                    * **stream** – Must be a valid CUDA stream if the memory type is GPU.

            inline explicit operator bool() const[#](#_CPPv4NK12tensorrt_llm8executor6TensorcvbEv "Link to this definition")

            inline bool operator==(*[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") const &rhs*) const[#](#_CPPv4NK12tensorrt_llm8executor6TensoreqERK6Tensor "Link to this definition")

            inline bool operator!=(*[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") const &rhs*) const[#](#_CPPv4NK12tensorrt_llm8executor6TensorneERK6Tensor "Link to this definition")

            Public Static Functions

            static [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") cpu(*[DataType](#_CPPv4N12tensorrt_llm8executor8DataTypeE "tensorrt_llm::executor::DataType") dataType*, *[Shape](#_CPPv4N12tensorrt_llm8executor5ShapeE "tensorrt_llm::executor::Shape") shape = {}*)[#](#_CPPv4N12tensorrt_llm8executor6Tensor3cpuE8DataType5Shape "Link to this definition")
            :   Allocate a cpu tensor with the given shape and data type.

                Parameters:
                :   * **shape** – The shape of the tensor.
                    * **dataType** – The data type of the tensor.

            template<typename T> static inline [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") cpu(*[Shape](#_CPPv4N12tensorrt_llm8executor5ShapeE "tensorrt_llm::executor::Shape") shape = {}*)[#](#_CPPv4I0EN12tensorrt_llm8executor6Tensor3cpuE6Tensor5Shape "Link to this definition")

            static [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") pinned(*[DataType](#_CPPv4N12tensorrt_llm8executor8DataTypeE "tensorrt_llm::executor::DataType") dataType*, *[Shape](#_CPPv4N12tensorrt_llm8executor5ShapeE "tensorrt_llm::executor::Shape") shape = {}*)[#](#_CPPv4N12tensorrt_llm8executor6Tensor6pinnedE8DataType5Shape "Link to this definition")
            :   Allocate a cpu tensor in pinned memory with the given shape and data type.

                Parameters:
                :   * **shape** – The shape of the tensor.
                    * **dataType** – The data type of the tensor.

            template<typename T> static inline [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") pinned(*[Shape](#_CPPv4N12tensorrt_llm8executor5ShapeE "tensorrt_llm::executor::Shape") shape = {}*)[#](#_CPPv4I0EN12tensorrt_llm8executor6Tensor6pinnedE6Tensor5Shape "Link to this definition")

            static [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") pooledPinned(*[DataType](#_CPPv4N12tensorrt_llm8executor8DataTypeE "tensorrt_llm::executor::DataType") dataType*, *[Shape](#_CPPv4N12tensorrt_llm8executor5ShapeE "tensorrt_llm::executor::Shape") shape = {}*)[#](#_CPPv4N12tensorrt_llm8executor6Tensor12pooledPinnedE8DataType5Shape "Link to this definition")
            :   Allocate a cpu tensor in pooled pinned memory with the given shape and data type.

                Parameters:
                :   * **shape** – The shape of the tensor.
                    * **dataType** – The data type of the tensor.

            template<typename T> static inline [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") pooledPinned( : *[Shape](#_CPPv4N12tensorrt_llm8executor5ShapeE "tensorrt_llm::executor::Shape") shape = {}*, )[#](#_CPPv4I0EN12tensorrt_llm8executor6Tensor12pooledPinnedE6Tensor5Shape "Link to this definition")

            static [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") managed(*[DataType](#_CPPv4N12tensorrt_llm8executor8DataTypeE "tensorrt_llm::executor::DataType") dataType*, *[Shape](#_CPPv4N12tensorrt_llm8executor5ShapeE "tensorrt_llm::executor::Shape") shape = {}*)[#](#_CPPv4N12tensorrt_llm8executor6Tensor7managedE8DataType5Shape "Link to this definition")
            :   Allocate a tensor in managed memory (UVM) with the given shape and data type.

                Parameters:
                :   * **shape** – The shape of the tensor.
                    * **dataType** – The data type of the tensor.

            template<typename T> static inline [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") managed(*[Shape](#_CPPv4N12tensorrt_llm8executor5ShapeE "tensorrt_llm::executor::Shape") shape = {}*)[#](#_CPPv4I0EN12tensorrt_llm8executor6Tensor7managedE6Tensor5Shape "Link to this definition")

            static [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") gpu( : *[DataType](#_CPPv4N12tensorrt_llm8executor8DataTypeE "tensorrt_llm::executor::DataType") dataType*, : *[CudaStreamPtr](#_CPPv4N12tensorrt_llm8executor6Tensor13CudaStreamPtrE "tensorrt_llm::executor::Tensor::CudaStreamPtr") stream*, : *[Shape](#_CPPv4N12tensorrt_llm8executor5ShapeE "tensorrt_llm::executor::Shape") shape = {}*, )[#](#_CPPv4N12tensorrt_llm8executor6Tensor3gpuE8DataType13CudaStreamPtr5Shape "Link to this definition")
            :   Allocate a gpu tensor with the given shape and data type on a particular cuda stream.

                Parameters:
                :   * **shape** – The shape of the tensor.
                    * **stream** – Specifies the CUDA stream on which to allocate the tensor for GPU memory.
                    * **dataType** – The data type of the tensor.

            template<typename T> static inline [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") gpu( : *[CudaStreamPtr](#_CPPv4N12tensorrt_llm8executor6Tensor13CudaStreamPtrE "tensorrt_llm::executor::Tensor::CudaStreamPtr") stream*, : *[Shape](#_CPPv4N12tensorrt_llm8executor5ShapeE "tensorrt_llm::executor::Shape") shape = {}*, )[#](#_CPPv4I0EN12tensorrt_llm8executor6Tensor3gpuE6Tensor13CudaStreamPtr5Shape "Link to this definition")

            static [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") of(*[DataType](#_CPPv4N12tensorrt_llm8executor8DataTypeE "tensorrt_llm::executor::DataType") dataType*, *void \*data*, *[Shape](#_CPPv4N12tensorrt_llm8executor5ShapeE "tensorrt_llm::executor::Shape") shape*)[#](#_CPPv4N12tensorrt_llm8executor6Tensor2ofE8DataTypePv5Shape "Link to this definition")
            :   Wrap a data pointer into a tensor without taking ownership.

                Parameters:
                :   * **shape** – The shape of the tensor.
                    * **dataType** – The data type of the tensor.
                    * **stream** – Specifies the CUDA stream on which to allocate the tensor for GPU memory.

            template<typename T> static inline [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") of(*[T](#_CPPv4I0EN12tensorrt_llm8executor6Tensor2ofE6TensorP1T5Shape "tensorrt_llm::executor::Tensor::of::T") \*data*, *[Shape](#_CPPv4N12tensorrt_llm8executor5ShapeE "tensorrt_llm::executor::Shape") shape*)[#](#_CPPv4I0EN12tensorrt_llm8executor6Tensor2ofE6TensorP1T5Shape "Link to this definition")
            :   Wrap a data pointer into a tensor without taking ownership.

                Parameters:
                :   * **shape** – The shape of the tensor.
                    * **dataType** – The data type of the tensor.
                    * **stream** – Specifies the CUDA stream on which to allocate the tensor for GPU memory.

            template<typename T> static inline [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") of(*[T](#_CPPv4I0EN12tensorrt_llm8executor6Tensor2ofE6TensorR1T "tensorrt_llm::executor::Tensor::of::T") &data*)[#](#_CPPv4I0EN12tensorrt_llm8executor6Tensor2ofE6TensorR1T "Link to this definition")
            :   Wrap any container into a tensor without taking ownership.

                Parameters:
                :   * **shape** – The shape of the tensor.
                    * **dataType** – The data type of the tensor.
                    * **stream** – Specifies the CUDA stream on which to allocate the tensor for GPU memory.

            Private Types

            using Impl = [runtime](#_CPPv4N12tensorrt_llm7runtimeE "tensorrt_llm::runtime")::[ITensor](runtime.md#_CPPv4N12tensorrt_llm7runtime7ITensorE "tensorrt_llm::runtime::ITensor")[#](#_CPPv4N12tensorrt_llm8executor6Tensor4ImplE "Link to this definition")

            Private Functions

            explicit Tensor(*std::shared\_ptr<[runtime](#_CPPv4N12tensorrt_llm7runtimeE "tensorrt_llm::runtime")::[ITensor](runtime.md#_CPPv4N12tensorrt_llm7runtime7ITensorE "tensorrt_llm::runtime::ITensor")> tensor*)[#](#_CPPv4N12tensorrt_llm8executor6Tensor6TensorENSt10shared_ptrIN7runtime7ITensorEEE "Link to this definition")

            [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") copyTo( : *std::shared\_ptr<[Impl](#_CPPv4N12tensorrt_llm8executor6Tensor4ImplE "tensorrt_llm::executor::Tensor::Impl")> tensor*, : *[CudaStreamPtr](#_CPPv4N12tensorrt_llm8executor6Tensor13CudaStreamPtrE "tensorrt_llm::executor::Tensor::CudaStreamPtr") stream*, ) const[#](#_CPPv4NK12tensorrt_llm8executor6Tensor6copyToENSt10shared_ptrI4ImplEE13CudaStreamPtr "Link to this definition")

            Private Members

            std::shared\_ptr<[Impl](#_CPPv4N12tensorrt_llm8executor6Tensor4ImplE "tensorrt_llm::executor::Tensor::Impl")> mTensor[#](#_CPPv4N12tensorrt_llm8executor6Tensor7mTensorE "Link to this definition")

            Private Static Functions

            template<typename T> static inline [DataType](#_CPPv4N12tensorrt_llm8executor8DataTypeE "tensorrt_llm::executor::DataType") getRuntimeType()[#](#_CPPv4I0EN12tensorrt_llm8executor6Tensor14getRuntimeTypeE8DataTypev "Link to this definition")

            Friends

            *friend class* Serialization

            friend std::shared\_ptr<[runtime](#_CPPv4N12tensorrt_llm7runtimeE "tensorrt_llm::runtime")::[ITensor](runtime.md#_CPPv4N12tensorrt_llm7runtime7ITensorE "tensorrt_llm::runtime::ITensor")> const &toITensor( : *[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") const &tensor*, )[#](#_CPPv4N12tensorrt_llm8executor6Tensor6detail9toITensorERK6Tensor "Link to this definition")

            friend [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") ofITensor( : *std::shared\_ptr<[runtime](#_CPPv4N12tensorrt_llm7runtimeE "tensorrt_llm::runtime")::[ITensor](runtime.md#_CPPv4N12tensorrt_llm7runtime7ITensorE "tensorrt_llm::runtime::ITensor")> tensor*, )[#](#_CPPv4N12tensorrt_llm8executor6Tensor6detail9ofITensorENSt10shared_ptrIN7runtime7ITensorEEE "Link to this definition")

        namespace detail[#](#_CPPv4N12tensorrt_llm8executor6detailE "Link to this definition")
        :   Typedefs

            using DimType64 = int64\_t[#](#_CPPv4N12tensorrt_llm8executor6detail9DimType64E "Link to this definition")

            Functions

            std::shared\_ptr<[runtime](#_CPPv4N12tensorrt_llm7runtimeE "tensorrt_llm::runtime")::[ITensor](runtime.md#_CPPv4N12tensorrt_llm7runtime7ITensorE "tensorrt_llm::runtime::ITensor")> const &toITensor( : *[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") const &tensor*, )[#](#_CPPv4N12tensorrt_llm8executor6detail9toITensorERK6Tensor "Link to this definition")

            [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") ofITensor(*std::shared\_ptr<[runtime](#_CPPv4N12tensorrt_llm7runtimeE "tensorrt_llm::runtime")::[ITensor](runtime.md#_CPPv4N12tensorrt_llm7runtime7ITensorE "tensorrt_llm::runtime::ITensor")> tensor*)[#](#_CPPv4N12tensorrt_llm8executor6detail9ofITensorENSt10shared_ptrIN7runtime7ITensorEEE "Link to this definition")

    namespace runtime[#](#_CPPv4N12tensorrt_llm7runtimeE "Link to this definition")

## transferAgent.h[#](#transferagent-h "Link to this heading")

namespace tensorrt\_llm
:   namespace executor
    :   namespace kv\_cache
        :   Typedefs

            using TransferDescs = [MemoryDescs](#_CPPv4N12tensorrt_llm8executor8kv_cache11MemoryDescsE "tensorrt_llm::executor::kv_cache::MemoryDescs")[#](#_CPPv4N12tensorrt_llm8executor8kv_cache13TransferDescsE "Link to this definition")

            using RegisterDescs = [MemoryDescs](#_CPPv4N12tensorrt_llm8executor8kv_cache11MemoryDescsE "tensorrt_llm::executor::kv_cache::MemoryDescs")[#](#_CPPv4N12tensorrt_llm8executor8kv_cache13RegisterDescsE "Link to this definition")

            using SyncMessage = std::string[#](#_CPPv4N12tensorrt_llm8executor8kv_cache11SyncMessageE "Link to this definition")

            using ConnectionInfoType = std::string[#](#_CPPv4N12tensorrt_llm8executor8kv_cache18ConnectionInfoTypeE "Link to this definition")

            Enums

            enum class MemoryType : uint8\_t[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryTypeE "Link to this definition")
            :   *Values:*

                enumerator kDRAM[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryType5kDRAME "Link to this definition")

                enumerator kVRAM[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryType5kVRAME "Link to this definition")

                enumerator kBLK[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryType4kBLKE "Link to this definition")

                enumerator kOBJ[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryType4kOBJE "Link to this definition")

                enumerator kFILE[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryType5kFILEE "Link to this definition")

            enum class TransferOp : uint8\_t[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10TransferOpE "Link to this definition")
            :   *Values:*

                enumerator kREAD[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10TransferOp5kREADE "Link to this definition")

                enumerator kWRITE[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10TransferOp6kWRITEE "Link to this definition")

            Functions

            template<typename ...Args> std::unique\_ptr<[BaseTransferAgent](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgentE "tensorrt_llm::executor::kv_cache::BaseTransferAgent")> makeTransferAgent( : *std::string const &backend*, : *[Args](#_CPPv4IDpEN12tensorrt_llm8executor8kv_cache17makeTransferAgentENSt10unique_ptrI17BaseTransferAgentEERKNSt6stringEDpRR4Args "tensorrt_llm::executor::kv_cache::makeTransferAgent::Args")&&... args*, )[#](#_CPPv4IDpEN12tensorrt_llm8executor8kv_cache17makeTransferAgentENSt10unique_ptrI17BaseTransferAgentEERKNSt6stringEDpRR4Args "Link to this definition")

            template<typename ...Args> std::shared\_ptr<[BaseLoopbackAgent](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseLoopbackAgentE "tensorrt_llm::executor::kv_cache::BaseLoopbackAgent")> makeLoopbackAgent( : *std::string const &backend*, : *[Args](#_CPPv4IDpEN12tensorrt_llm8executor8kv_cache17makeLoopbackAgentENSt10shared_ptrI17BaseLoopbackAgentEERKNSt6stringEDpRR4Args "tensorrt_llm::executor::kv_cache::makeLoopbackAgent::Args")&&... args*, )[#](#_CPPv4IDpEN12tensorrt_llm8executor8kv_cache17makeLoopbackAgentENSt10shared_ptrI17BaseLoopbackAgentEERKNSt6stringEDpRR4Args "Link to this definition")

            class AgentDesc[#](#_CPPv4N12tensorrt_llm8executor8kv_cache9AgentDescE "Link to this definition")
            :   Public Functions

                inline AgentDesc(*std::string backendAgentDesc*)[#](#_CPPv4N12tensorrt_llm8executor8kv_cache9AgentDesc9AgentDescENSt6stringE "Link to this definition")

                inline std::string const &getBackendAgentDesc() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache9AgentDesc19getBackendAgentDescEv "Link to this definition")

                Private Members

                std::string mBackendAgentDesc[#](#_CPPv4N12tensorrt_llm8executor8kv_cache9AgentDesc17mBackendAgentDescE "Link to this definition")

            struct BaseAgentConfig[#](#_CPPv4N12tensorrt_llm8executor8kv_cache15BaseAgentConfigE "Link to this definition")
            :   Public Members

                std::string mName[#](#_CPPv4N12tensorrt_llm8executor8kv_cache15BaseAgentConfig5mNameE "Link to this definition")

                bool useProgThread[#](#_CPPv4N12tensorrt_llm8executor8kv_cache15BaseAgentConfig13useProgThreadE "Link to this definition")

                bool multiThread[#](#_CPPv4N12tensorrt_llm8executor8kv_cache15BaseAgentConfig11multiThreadE "Link to this definition")

            class BaseLoopbackAgent[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseLoopbackAgentE "Link to this definition")
            :   Public Functions

                virtual ~BaseLoopbackAgent() = default[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseLoopbackAgentD0Ev "Link to this definition")

                virtual void executeLoopbackRequest( : *[MemoryDescs](#_CPPv4N12tensorrt_llm8executor8kv_cache11MemoryDescsE "tensorrt_llm::executor::kv_cache::MemoryDescs") const &memoryDescs*, : *[FileDescs](#_CPPv4N12tensorrt_llm8executor8kv_cache9FileDescsE "tensorrt_llm::executor::kv_cache::FileDescs") const &fileDescs*, : *bool isOffload*, ) = 0[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseLoopbackAgent22executeLoopbackRequestERK11MemoryDescsRK9FileDescsb "Link to this definition")

            class BaseTransferAgent[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgentE "Link to this definition")
            :   Public Functions

                virtual ~BaseTransferAgent() = default[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgentD0Ev "Link to this definition")

                virtual void registerMemory(*[RegisterDescs](#_CPPv4N12tensorrt_llm8executor8kv_cache13RegisterDescsE "tensorrt_llm::executor::kv_cache::RegisterDescs") const &descs*) = 0[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent14registerMemoryERK13RegisterDescs "Link to this definition")

                virtual void deregisterMemory(*[RegisterDescs](#_CPPv4N12tensorrt_llm8executor8kv_cache13RegisterDescsE "tensorrt_llm::executor::kv_cache::RegisterDescs") const &descs*) = 0[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent16deregisterMemoryERK13RegisterDescs "Link to this definition")

                virtual void loadRemoteAgent( : *std::string const &name*, : *[AgentDesc](#_CPPv4N12tensorrt_llm8executor8kv_cache9AgentDescE "tensorrt_llm::executor::kv_cache::AgentDesc") const &agentDesc*, ) = 0[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent15loadRemoteAgentERKNSt6stringERK9AgentDesc "Link to this definition")

                virtual [AgentDesc](#_CPPv4N12tensorrt_llm8executor8kv_cache9AgentDescE "tensorrt_llm::executor::kv_cache::AgentDesc") getLocalAgentDesc() = 0[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent17getLocalAgentDescEv "Link to this definition")

                virtual void invalidateRemoteAgent(*std::string const &name*) = 0[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent21invalidateRemoteAgentERKNSt6stringE "Link to this definition")

                virtual std::unique\_ptr<[TransferStatus](#_CPPv4N12tensorrt_llm8executor8kv_cache14TransferStatusE "tensorrt_llm::executor::kv_cache::TransferStatus")> submitTransferRequests( : *[TransferRequest](#_CPPv4N12tensorrt_llm8executor8kv_cache15TransferRequestE "tensorrt_llm::executor::kv_cache::TransferRequest") const &request*, ) = 0[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent22submitTransferRequestsERK15TransferRequest "Link to this definition")

                virtual void notifySyncMessage( : *std::string const &name*, : *[SyncMessage](#_CPPv4N12tensorrt_llm8executor8kv_cache11SyncMessageE "tensorrt_llm::executor::kv_cache::SyncMessage") const &syncMessage*, ) = 0[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent17notifySyncMessageERKNSt6stringERK11SyncMessage "Link to this definition")

                virtual std::unordered\_map<std::string, std::vector<[SyncMessage](#_CPPv4N12tensorrt_llm8executor8kv_cache11SyncMessageE "tensorrt_llm::executor::kv_cache::SyncMessage")>> getNotifiedSyncMessages() = 0[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent23getNotifiedSyncMessagesEv "Link to this definition")

                virtual [ConnectionInfoType](#_CPPv4N12tensorrt_llm8executor8kv_cache18ConnectionInfoTypeE "tensorrt_llm::executor::kv_cache::ConnectionInfoType") getConnectionInfo() = 0[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent17getConnectionInfoEv "Link to this definition")

                virtual void connectRemoteAgent( : *std::string const &name*, : *[ConnectionInfoType](#_CPPv4N12tensorrt_llm8executor8kv_cache18ConnectionInfoTypeE "tensorrt_llm::executor::kv_cache::ConnectionInfoType") const &connectionInfo*, ) = 0[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent18connectRemoteAgentERKNSt6stringERK18ConnectionInfoType "Link to this definition")

                virtual bool checkRemoteDescs( : *std::string const &name*, : *[MemoryDescs](#_CPPv4N12tensorrt_llm8executor8kv_cache11MemoryDescsE "tensorrt_llm::executor::kv_cache::MemoryDescs") const &memoryDescs*, ) = 0[#](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent16checkRemoteDescsERKNSt6stringERK11MemoryDescs "Link to this definition")

            class DynLibLoader[#](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoaderE "Link to this definition")
            :   Public Functions

                void \*getHandle(*std::string const &name*)[#](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoader9getHandleERKNSt6stringE "Link to this definition")

                template<typename FunctionT> inline [FunctionT](#_CPPv4I0EN12tensorrt_llm8executor8kv_cache12DynLibLoader18getFunctionPointerE9FunctionTRKNSt6stringERKNSt6stringE "tensorrt_llm::executor::kv_cache::DynLibLoader::getFunctionPointer::FunctionT") getFunctionPointer( : *std::string const &libName*, : *std::string const &funcName*, )[#](#_CPPv4I0EN12tensorrt_llm8executor8kv_cache12DynLibLoader18getFunctionPointerE9FunctionTRKNSt6stringERKNSt6stringE "Link to this definition")

                ~DynLibLoader()[#](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoaderD0Ev "Link to this definition")

                DynLibLoader() = default[#](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoader12DynLibLoaderEv "Link to this definition")

                DynLibLoader(*[DynLibLoader](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoader12DynLibLoaderERK12DynLibLoader "tensorrt_llm::executor::kv_cache::DynLibLoader::DynLibLoader") const&*) = delete[#](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoader12DynLibLoaderERK12DynLibLoader "Link to this definition")

                [DynLibLoader](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoaderE "tensorrt_llm::executor::kv_cache::DynLibLoader") &operator=(*[DynLibLoader](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoaderE "tensorrt_llm::executor::kv_cache::DynLibLoader") const&*) = delete[#](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoaderaSERK12DynLibLoader "Link to this definition")

                Public Static Functions

                static [DynLibLoader](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoaderE "tensorrt_llm::executor::kv_cache::DynLibLoader") &getInstance()[#](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoader11getInstanceEv "Link to this definition")

                Private Members

                std::mutex mDllMutex[#](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoader9mDllMutexE "Link to this definition")

                std::unordered\_map<std::string, void\*> mHandlers[#](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoader9mHandlersE "Link to this definition")

                Private Static Functions

                static void \*dlSym(*void \*handle*, *char const \*symbol*)[#](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoader5dlSymEPvPKc "Link to this definition")

            class FileDesc[#](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDescE "Link to this definition")
            :   Public Functions

                inline FileDesc( : *std::string const &filename*, : *int flags*, : *mode\_t mode*, : *size\_t len*, )[#](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDesc8FileDescERKNSt6stringEi6mode_t6size_t "Link to this definition")

                inline FileDesc(*[FileDesc](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDesc8FileDescERR8FileDesc "tensorrt_llm::executor::kv_cache::FileDesc::FileDesc") &&other*) noexcept[#](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDesc8FileDescERR8FileDesc "Link to this definition")

                inline [FileDesc](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDescE "tensorrt_llm::executor::kv_cache::FileDesc") &operator=(*[FileDesc](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDescE "tensorrt_llm::executor::kv_cache::FileDesc") &&other*) noexcept[#](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDescaSERR8FileDesc "Link to this definition")

                inline ~FileDesc()[#](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDescD0Ev "Link to this definition")

                inline uint64\_t getFd() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache8FileDesc5getFdEv "Link to this definition")

                inline size\_t getLen() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache8FileDesc6getLenEv "Link to this definition")

                FileDesc(*[FileDesc](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDesc8FileDescERK8FileDesc "tensorrt_llm::executor::kv_cache::FileDesc::FileDesc") const&*) = delete[#](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDesc8FileDescERK8FileDesc "Link to this definition")

                [FileDesc](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDescE "tensorrt_llm::executor::kv_cache::FileDesc") &operator=(*[FileDesc](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDescE "tensorrt_llm::executor::kv_cache::FileDesc") const&*) = delete[#](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDescaSERK8FileDesc "Link to this definition")

                Private Members

                int fd[#](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDesc2fdE "Link to this definition")

                size\_t mLen[#](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDesc4mLenE "Link to this definition")

            class FileDescs[#](#_CPPv4N12tensorrt_llm8executor8kv_cache9FileDescsE "Link to this definition")
            :   Public Functions

                inline FileDescs(*std::vector<[FileDesc](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDescE "tensorrt_llm::executor::kv_cache::FileDesc")> &&descs*)[#](#_CPPv4N12tensorrt_llm8executor8kv_cache9FileDescs9FileDescsERRNSt6vectorI8FileDescEE "Link to this definition")

                inline std::vector<[FileDesc](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDescE "tensorrt_llm::executor::kv_cache::FileDesc")> const &getDescs() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache9FileDescs8getDescsEv "Link to this definition")

                Private Members

                std::vector<[FileDesc](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDescE "tensorrt_llm::executor::kv_cache::FileDesc")> mDescs[#](#_CPPv4N12tensorrt_llm8executor8kv_cache9FileDescs6mDescsE "Link to this definition")

            class MemoryDesc[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDescE "Link to this definition")
            :   Public Functions

                inline MemoryDesc( : *std::vector<char> const &vec*, : *uint32\_t deviceId = 0*, )[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDesc10MemoryDescERKNSt6vectorIcEE8uint32_t "Link to this definition")

                inline MemoryDesc(*void \*addr*, *size\_t len*, *uint32\_t deviceId*)[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDesc10MemoryDescEPv6size_t8uint32_t "Link to this definition")

                inline MemoryDesc(*uintptr\_t addr*, *size\_t len*, *uint32\_t deviceId*)[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDesc10MemoryDescE9uintptr_t6size_t8uint32_t "Link to this definition")

                inline uintptr\_t getAddr() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache10MemoryDesc7getAddrEv "Link to this definition")

                inline size\_t getLen() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache10MemoryDesc6getLenEv "Link to this definition")

                inline uint32\_t getDeviceId() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache10MemoryDesc11getDeviceIdEv "Link to this definition")

                Public Static Functions

                static void serialize(*[MemoryDesc](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDescE "tensorrt_llm::executor::kv_cache::MemoryDesc") const &memoryDesc*, *std::ostream &os*)[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDesc9serializeERK10MemoryDescRNSt7ostreamE "Link to this definition")

                static [MemoryDesc](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDescE "tensorrt_llm::executor::kv_cache::MemoryDesc") deserialize(*std::istream &is*)[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDesc11deserializeERNSt7istreamE "Link to this definition")

                static size\_t serializedSize(*[MemoryDesc](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDescE "tensorrt_llm::executor::kv_cache::MemoryDesc") const &memoryDesc*)[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDesc14serializedSizeERK10MemoryDesc "Link to this definition")

                Private Members

                uintptr\_t mAddr[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDesc5mAddrE "Link to this definition")

                size\_t mLen[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDesc4mLenE "Link to this definition")

                uint32\_t mDeviceId[#](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDesc9mDeviceIdE "Link to this definition")

            class MemoryDescs[#](#_CPPv4N12tensorrt_llm8executor8kv_cache11MemoryDescsE "Link to this definition")
            :   Public Functions

                inline MemoryDescs(*[MemoryType](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryTypeE "tensorrt_llm::executor::kv_cache::MemoryType") type*, *std::vector<[MemoryDesc](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDescE "tensorrt_llm::executor::kv_cache::MemoryDesc")> descs*)[#](#_CPPv4N12tensorrt_llm8executor8kv_cache11MemoryDescs11MemoryDescsE10MemoryTypeNSt6vectorI10MemoryDescEE "Link to this definition")

                inline [MemoryType](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryTypeE "tensorrt_llm::executor::kv_cache::MemoryType") getType() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache11MemoryDescs7getTypeEv "Link to this definition")

                inline std::vector<[MemoryDesc](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDescE "tensorrt_llm::executor::kv_cache::MemoryDesc")> const &getDescs() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache11MemoryDescs8getDescsEv "Link to this definition")

                Private Members

                [MemoryType](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryTypeE "tensorrt_llm::executor::kv_cache::MemoryType") mType[#](#_CPPv4N12tensorrt_llm8executor8kv_cache11MemoryDescs5mTypeE "Link to this definition")

                std::vector<[MemoryDesc](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDescE "tensorrt_llm::executor::kv_cache::MemoryDesc")> mDescs[#](#_CPPv4N12tensorrt_llm8executor8kv_cache11MemoryDescs6mDescsE "Link to this definition")

            class TransferRequest[#](#_CPPv4N12tensorrt_llm8executor8kv_cache15TransferRequestE "Link to this definition")
            :   Public Functions

                inline TransferRequest( : *[TransferOp](#_CPPv4N12tensorrt_llm8executor8kv_cache10TransferOpE "tensorrt_llm::executor::kv_cache::TransferOp") op*, : *[TransferDescs](#_CPPv4N12tensorrt_llm8executor8kv_cache13TransferDescsE "tensorrt_llm::executor::kv_cache::TransferDescs") srcDescs*, : *[TransferDescs](#_CPPv4N12tensorrt_llm8executor8kv_cache13TransferDescsE "tensorrt_llm::executor::kv_cache::TransferDescs") dstDescs*, : *std::string const &remoteName*, : *std::optional<[SyncMessage](#_CPPv4N12tensorrt_llm8executor8kv_cache11SyncMessageE "tensorrt_llm::executor::kv_cache::SyncMessage")> syncMessage = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor8kv_cache15TransferRequest15TransferRequestE10TransferOp13TransferDescs13TransferDescsRKNSt6stringENSt8optionalI11SyncMessageEE "Link to this definition")

                inline [TransferOp](#_CPPv4N12tensorrt_llm8executor8kv_cache10TransferOpE "tensorrt_llm::executor::kv_cache::TransferOp") getOp() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache15TransferRequest5getOpEv "Link to this definition")

                inline [TransferDescs](#_CPPv4N12tensorrt_llm8executor8kv_cache13TransferDescsE "tensorrt_llm::executor::kv_cache::TransferDescs") const &getSrcDescs() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache15TransferRequest11getSrcDescsEv "Link to this definition")

                inline [TransferDescs](#_CPPv4N12tensorrt_llm8executor8kv_cache13TransferDescsE "tensorrt_llm::executor::kv_cache::TransferDescs") const &getDstDescs() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache15TransferRequest11getDstDescsEv "Link to this definition")

                inline std::string const &getRemoteName() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache15TransferRequest13getRemoteNameEv "Link to this definition")

                inline std::optional<[SyncMessage](#_CPPv4N12tensorrt_llm8executor8kv_cache11SyncMessageE "tensorrt_llm::executor::kv_cache::SyncMessage")> getSyncMessage() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache15TransferRequest14getSyncMessageEv "Link to this definition")

                Private Members

                [TransferOp](#_CPPv4N12tensorrt_llm8executor8kv_cache10TransferOpE "tensorrt_llm::executor::kv_cache::TransferOp") mOp[#](#_CPPv4N12tensorrt_llm8executor8kv_cache15TransferRequest3mOpE "Link to this definition")

                [TransferDescs](#_CPPv4N12tensorrt_llm8executor8kv_cache13TransferDescsE "tensorrt_llm::executor::kv_cache::TransferDescs") mSrcDescs[#](#_CPPv4N12tensorrt_llm8executor8kv_cache15TransferRequest9mSrcDescsE "Link to this definition")

                [TransferDescs](#_CPPv4N12tensorrt_llm8executor8kv_cache13TransferDescsE "tensorrt_llm::executor::kv_cache::TransferDescs") mDstDescs[#](#_CPPv4N12tensorrt_llm8executor8kv_cache15TransferRequest9mDstDescsE "Link to this definition")

                std::string mRemoteName[#](#_CPPv4N12tensorrt_llm8executor8kv_cache15TransferRequest11mRemoteNameE "Link to this definition")

                std::optional<[SyncMessage](#_CPPv4N12tensorrt_llm8executor8kv_cache11SyncMessageE "tensorrt_llm::executor::kv_cache::SyncMessage")> mSyncMessage[#](#_CPPv4N12tensorrt_llm8executor8kv_cache15TransferRequest12mSyncMessageE "Link to this definition")

            class TransferStatus[#](#_CPPv4N12tensorrt_llm8executor8kv_cache14TransferStatusE "Link to this definition")
            :   Public Functions

                virtual ~TransferStatus() = default[#](#_CPPv4N12tensorrt_llm8executor8kv_cache14TransferStatusD0Ev "Link to this definition")

                virtual bool isCompleted() const = 0[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache14TransferStatus11isCompletedEv "Link to this definition")

                virtual void wait() const = 0[#](#_CPPv4NK12tensorrt_llm8executor8kv_cache14TransferStatus4waitEv "Link to this definition")

## executor.h[#](#executor-h "Link to this heading")

namespace tensorrt\_llm
:   namespace batch\_manager[#](#_CPPv4N12tensorrt_llm13batch_managerE "Link to this definition")
    :   namespace kv\_cache\_manager[#](#_CPPv4N12tensorrt_llm13batch_manager16kv_cache_managerE "Link to this definition")

    namespace executor
    :   Typedefs

        using RetentionPriority = [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")[#](#_CPPv4N12tensorrt_llm8executor17RetentionPriorityE "Link to this definition")

        using KVCacheEventData = std::variant<[KVCacheCreatedData](#_CPPv4N12tensorrt_llm8executor18KVCacheCreatedDataE "tensorrt_llm::executor::KVCacheCreatedData"), [KVCacheStoredData](#_CPPv4N12tensorrt_llm8executor17KVCacheStoredDataE "tensorrt_llm::executor::KVCacheStoredData"), [KVCacheRemovedData](#_CPPv4N12tensorrt_llm8executor18KVCacheRemovedDataE "tensorrt_llm::executor::KVCacheRemovedData"), [KVCacheUpdatedData](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedDataE "tensorrt_llm::executor::KVCacheUpdatedData")>[#](#_CPPv4N12tensorrt_llm8executor16KVCacheEventDataE "Link to this definition")

        Functions

        char const \*version() noexcept[#](#_CPPv4N12tensorrt_llm8executor7versionEv "Link to this definition")
        :   Version of TRT-LLM.

        class AdditionalModelOutput[#](#_CPPv4N12tensorrt_llm8executor21AdditionalModelOutputE "Link to this definition")
        :   *#include <executor.h>*

            Additional output that should be gathered.

            By default gather output of shape [beamWidth, x] from each generation phase. If gatherContext is true, also gather output of shape [promptLen, x] from context phase.

            Public Functions

            explicit AdditionalModelOutput( : *std::string name*, : *bool gatherContext = false*, )[#](#_CPPv4N12tensorrt_llm8executor21AdditionalModelOutput21AdditionalModelOutputENSt6stringEb "Link to this definition")

            bool operator==(*[AdditionalModelOutput](#_CPPv4N12tensorrt_llm8executor21AdditionalModelOutputE "tensorrt_llm::executor::AdditionalModelOutput") const &other*) const[#](#_CPPv4NK12tensorrt_llm8executor21AdditionalModelOutputeqERK21AdditionalModelOutput "Link to this definition")

            Public Members

            std::string name[#](#_CPPv4N12tensorrt_llm8executor21AdditionalModelOutput4nameE "Link to this definition")

            bool gatherContext = {false}[#](#_CPPv4N12tensorrt_llm8executor21AdditionalModelOutput13gatherContextE "Link to this definition")

        struct AdditionalOutput[#](#_CPPv4N12tensorrt_llm8executor16AdditionalOutputE "Link to this definition")
        :   Public Functions

            inline AdditionalOutput(*std::string name*, *[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") output*)[#](#_CPPv4N12tensorrt_llm8executor16AdditionalOutput16AdditionalOutputENSt6stringE6Tensor "Link to this definition")

            AdditionalOutput(*[AdditionalOutput](#_CPPv4N12tensorrt_llm8executor16AdditionalOutput16AdditionalOutputERK16AdditionalOutput "tensorrt_llm::executor::AdditionalOutput::AdditionalOutput") const &other*) = default[#](#_CPPv4N12tensorrt_llm8executor16AdditionalOutput16AdditionalOutputERK16AdditionalOutput "Link to this definition")

            AdditionalOutput(*[AdditionalOutput](#_CPPv4N12tensorrt_llm8executor16AdditionalOutput16AdditionalOutputERR16AdditionalOutput "tensorrt_llm::executor::AdditionalOutput::AdditionalOutput") &&other*) noexcept = default[#](#_CPPv4N12tensorrt_llm8executor16AdditionalOutput16AdditionalOutputERR16AdditionalOutput "Link to this definition")

            [AdditionalOutput](#_CPPv4N12tensorrt_llm8executor16AdditionalOutputE "tensorrt_llm::executor::AdditionalOutput") &operator=(*[AdditionalOutput](#_CPPv4N12tensorrt_llm8executor16AdditionalOutputE "tensorrt_llm::executor::AdditionalOutput") const &other*) = default[#](#_CPPv4N12tensorrt_llm8executor16AdditionalOutputaSERK16AdditionalOutput "Link to this definition")

            [AdditionalOutput](#_CPPv4N12tensorrt_llm8executor16AdditionalOutputE "tensorrt_llm::executor::AdditionalOutput") &operator=( : *[AdditionalOutput](#_CPPv4N12tensorrt_llm8executor16AdditionalOutputE "tensorrt_llm::executor::AdditionalOutput") &&other*, ) noexcept = default[#](#_CPPv4N12tensorrt_llm8executor16AdditionalOutputaSERR16AdditionalOutput "Link to this definition")

            ~AdditionalOutput() = default[#](#_CPPv4N12tensorrt_llm8executor16AdditionalOutputD0Ev "Link to this definition")

            Public Members

            std::string name[#](#_CPPv4N12tensorrt_llm8executor16AdditionalOutput4nameE "Link to this definition")

            [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") output[#](#_CPPv4N12tensorrt_llm8executor16AdditionalOutput6outputE "Link to this definition")

        class CacheTransceiverConfig[#](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfigE "Link to this definition")
        :   Public Types

            enum class BackendType : std::uint8\_t[#](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig11BackendTypeE "Link to this definition")
            :   *Values:*

                enumerator DEFAULT[#](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig11BackendType7DEFAULTE "Link to this definition")

                enumerator MPI[#](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig11BackendType3MPIE "Link to this definition")

                enumerator UCX[#](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig11BackendType3UCXE "Link to this definition")

                enumerator NIXL[#](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig11BackendType4NIXLE "Link to this definition")

            Public Functions

            explicit CacheTransceiverConfig( : *std::optional<[BackendType](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig11BackendTypeE "tensorrt_llm::executor::CacheTransceiverConfig::BackendType")> backendType = std::nullopt*, : *std::optional<size\_t> maxNumTokens = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig22CacheTransceiverConfigENSt8optionalI11BackendTypeEENSt8optionalI6size_tEE "Link to this definition")

            bool operator==(*[CacheTransceiverConfig](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfigE "tensorrt_llm::executor::CacheTransceiverConfig") const &other*) const[#](#_CPPv4NK12tensorrt_llm8executor22CacheTransceiverConfigeqERK22CacheTransceiverConfig "Link to this definition")

            void setBackendType(*std::optional<[BackendType](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig11BackendTypeE "tensorrt_llm::executor::CacheTransceiverConfig::BackendType")> backendType*)[#](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig14setBackendTypeENSt8optionalI11BackendTypeEE "Link to this definition")

            void setMaxTokensInBuffer(*std::optional<size\_t> maxTokensInBuffer*)[#](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig20setMaxTokensInBufferENSt8optionalI6size_tEE "Link to this definition")

            std::optional<size\_t> getMaxTokensInBuffer() const[#](#_CPPv4NK12tensorrt_llm8executor22CacheTransceiverConfig20getMaxTokensInBufferEv "Link to this definition")

            std::optional<[BackendType](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig11BackendTypeE "tensorrt_llm::executor::CacheTransceiverConfig::BackendType")> getBackendType() const[#](#_CPPv4NK12tensorrt_llm8executor22CacheTransceiverConfig14getBackendTypeEv "Link to this definition")

            Private Members

            std::optional<[BackendType](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig11BackendTypeE "tensorrt_llm::executor::CacheTransceiverConfig::BackendType")> mBackendType[#](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig12mBackendTypeE "Link to this definition")

            std::optional<size\_t> mMaxTokensInBuffer[#](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig18mMaxTokensInBufferE "Link to this definition")
            :   The maximum number of tokens that the CacheTransceiver’s pre-allocated buffer can hold. If the number of kvCache tokens to be transferred for a single request is greater than this value, the performance of the cache transfer may be degraded.

        class ContextPhaseParams[#](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsE "Link to this definition")
        :   Public Types

            using RequestIdType = std::uint64\_t[#](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams13RequestIdTypeE "Link to this definition")

            Public Functions

            ContextPhaseParams( : *[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens") firstGenTokens*, : *[RequestIdType](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams13RequestIdTypeE "tensorrt_llm::executor::ContextPhaseParams::RequestIdType") reqId*, : *std::optional<[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens")> draftTokens*, )[#](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams18ContextPhaseParamsE9VecTokens13RequestIdTypeNSt8optionalI9VecTokensEE "Link to this definition")

            ContextPhaseParams( : *[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens") firstGenTokens*, : *[RequestIdType](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams13RequestIdTypeE "tensorrt_llm::executor::ContextPhaseParams::RequestIdType") reqId*, : *void \*state*, : *std::optional<[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens")> draftTokens*, )[#](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams18ContextPhaseParamsE9VecTokens13RequestIdTypePvNSt8optionalI9VecTokensEE "Link to this definition")

            ContextPhaseParams( : *[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens") firstGenTokens*, : *[RequestIdType](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams13RequestIdTypeE "tensorrt_llm::executor::ContextPhaseParams::RequestIdType") reqId*, : *std::vector<char> const &serializedState*, : *std::optional<[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens")> draftTokens*, )[#](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams18ContextPhaseParamsE9VecTokens13RequestIdTypeRKNSt6vectorIcEENSt8optionalI9VecTokensEE "Link to this definition")

            ContextPhaseParams(*[ContextPhaseParams](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams18ContextPhaseParamsERK18ContextPhaseParams "tensorrt_llm::executor::ContextPhaseParams::ContextPhaseParams") const&*)[#](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams18ContextPhaseParamsERK18ContextPhaseParams "Link to this definition")

            ContextPhaseParams(*[ContextPhaseParams](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams18ContextPhaseParamsERR18ContextPhaseParams "tensorrt_llm::executor::ContextPhaseParams::ContextPhaseParams")&&*) noexcept[#](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams18ContextPhaseParamsERR18ContextPhaseParams "Link to this definition")

            [ContextPhaseParams](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsE "tensorrt_llm::executor::ContextPhaseParams") &operator=(*[ContextPhaseParams](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsE "tensorrt_llm::executor::ContextPhaseParams") const&*)[#](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsaSERK18ContextPhaseParams "Link to this definition")

            [ContextPhaseParams](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsE "tensorrt_llm::executor::ContextPhaseParams") &operator=(*[ContextPhaseParams](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsE "tensorrt_llm::executor::ContextPhaseParams")&&*) noexcept[#](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsaSERR18ContextPhaseParams "Link to this definition")

            ~ContextPhaseParams()[#](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsD0Ev "Link to this definition")

            bool operator==(*[ContextPhaseParams](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsE "tensorrt_llm::executor::ContextPhaseParams") const&*) const noexcept[#](#_CPPv4NK12tensorrt_llm8executor18ContextPhaseParamseqERK18ContextPhaseParams "Link to this definition")

            [VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens") const &getFirstGenTokens() const & noexcept[#](#_CPPv4NKR12tensorrt_llm8executor18ContextPhaseParams17getFirstGenTokensEv "Link to this definition")

            std::optional<[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens")> const &getDraftTokens() const & noexcept[#](#_CPPv4NKR12tensorrt_llm8executor18ContextPhaseParams14getDraftTokensEv "Link to this definition")

            [VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens") popFirstGenTokens() && noexcept[#](#_CPPv4NO12tensorrt_llm8executor18ContextPhaseParams17popFirstGenTokensEv "Link to this definition")

            [RequestIdType](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams13RequestIdTypeE "tensorrt_llm::executor::ContextPhaseParams::RequestIdType") getReqId() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor18ContextPhaseParams8getReqIdEv "Link to this definition")

            void const \*getState() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor18ContextPhaseParams8getStateEv "Link to this definition")

            void \*getState() noexcept[#](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams8getStateEv "Link to this definition")

            void \*releaseState() noexcept[#](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams12releaseStateEv "Link to this definition")

            std::vector<char> getSerializedState() const noexcept[#](#_CPPv4NK12tensorrt_llm8executor18ContextPhaseParams18getSerializedStateEv "Link to this definition")

            Private Types

            using StatePtr = std::unique\_ptr<void, decltype(&[deleter](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams7deleterEPKv "tensorrt_llm::executor::ContextPhaseParams::deleter"))>[#](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams8StatePtrE "Link to this definition")

            Private Members

            [RequestIdType](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams13RequestIdTypeE "tensorrt_llm::executor::ContextPhaseParams::RequestIdType") mReqId = {0}[#](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams6mReqIdE "Link to this definition")
            :   This request corresponds to the request ID in the context phase.

            [VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens") mFirstGenTokens[#](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams15mFirstGenTokensE "Link to this definition")
            :   The first tokens generated by context executor.

            [StatePtr](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams8StatePtrE "tensorrt_llm::executor::ContextPhaseParams::StatePtr") mState = {nullptr, [deleter](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams7deleterEPKv "tensorrt_llm::executor::ContextPhaseParams::deleter")}[#](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams6mStateE "Link to this definition")
            :   Context phase state of this request.

            std::optional<[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens")> mDraftTokens[#](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams12mDraftTokensE "Link to this definition")
            :   The draft tokens generated by context executor.

            Private Static Functions

            static void deleter(*void const \*data*)[#](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams7deleterEPKv "Link to this definition")

            Friends

            *friend class* Serialization

        class DebugConfig[#](#_CPPv4N12tensorrt_llm8executor11DebugConfigE "Link to this definition")
        :   *#include <executor.h>*

            Configuration class for debugging output.

            Public Functions

            explicit DebugConfig( : *bool debugInputTensors = false*, : *bool debugOutputTensors = false*, : *[StringVec](#_CPPv4N12tensorrt_llm8executor11DebugConfig9StringVecE "tensorrt_llm::executor::DebugConfig::StringVec") debugTensorNames = {}*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") debugTensorsMaxIterations = 0*, )[#](#_CPPv4N12tensorrt_llm8executor11DebugConfig11DebugConfigEbb9StringVec10SizeType32 "Link to this definition")

            bool operator==(*[DebugConfig](#_CPPv4N12tensorrt_llm8executor11DebugConfigE "tensorrt_llm::executor::DebugConfig") const &other*) const[#](#_CPPv4NK12tensorrt_llm8executor11DebugConfigeqERK11DebugConfig "Link to this definition")

            bool getDebugInputTensors() const[#](#_CPPv4NK12tensorrt_llm8executor11DebugConfig20getDebugInputTensorsEv "Link to this definition")

            bool getDebugOutputTensors() const[#](#_CPPv4NK12tensorrt_llm8executor11DebugConfig21getDebugOutputTensorsEv "Link to this definition")

            [StringVec](#_CPPv4N12tensorrt_llm8executor11DebugConfig9StringVecE "tensorrt_llm::executor::DebugConfig::StringVec") const &getDebugTensorNames() const[#](#_CPPv4NK12tensorrt_llm8executor11DebugConfig19getDebugTensorNamesEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getDebugTensorsMaxIterations() const[#](#_CPPv4NK12tensorrt_llm8executor11DebugConfig28getDebugTensorsMaxIterationsEv "Link to this definition")

            void setDebugInputTensors(*bool debugInputTensors*)[#](#_CPPv4N12tensorrt_llm8executor11DebugConfig20setDebugInputTensorsEb "Link to this definition")

            void setDebugOutputTensors(*bool debugOutputTensors*)[#](#_CPPv4N12tensorrt_llm8executor11DebugConfig21setDebugOutputTensorsEb "Link to this definition")

            void setDebugTensorNames(*[StringVec](#_CPPv4N12tensorrt_llm8executor11DebugConfig9StringVecE "tensorrt_llm::executor::DebugConfig::StringVec") const &debugTensorNames*)[#](#_CPPv4N12tensorrt_llm8executor11DebugConfig19setDebugTensorNamesERK9StringVec "Link to this definition")

            void setDebugTensorsMaxIterations( : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") debugTensorsMaxIterations*, )[#](#_CPPv4N12tensorrt_llm8executor11DebugConfig28setDebugTensorsMaxIterationsE10SizeType32 "Link to this definition")

            Private Types

            using StringVec = std::vector<std::string>[#](#_CPPv4N12tensorrt_llm8executor11DebugConfig9StringVecE "Link to this definition")

            Private Members

            bool mDebugInputTensors[#](#_CPPv4N12tensorrt_llm8executor11DebugConfig18mDebugInputTensorsE "Link to this definition")
            :   If true, debug all input tensors.

            bool mDebugOutputTensors[#](#_CPPv4N12tensorrt_llm8executor11DebugConfig19mDebugOutputTensorsE "Link to this definition")
            :   If true, debug all output tensors.

            [StringVec](#_CPPv4N12tensorrt_llm8executor11DebugConfig9StringVecE "tensorrt_llm::executor::DebugConfig::StringVec") mDebugTensorNames[#](#_CPPv4N12tensorrt_llm8executor11DebugConfig17mDebugTensorNamesE "Link to this definition")
            :   If not empty, only debug tensors in this list.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mDebugTensorsMaxIterations[#](#_CPPv4N12tensorrt_llm8executor11DebugConfig26mDebugTensorsMaxIterationsE "Link to this definition")
            :   If > 0, provide debug tensors for at most debugTensorsMaxIterations past iterations, else dump them to files.

            Friends

            *friend class* Serialization

        class DecodingConfig[#](#_CPPv4N12tensorrt_llm8executor14DecodingConfigE "Link to this definition")
        :   *#include <executor.h>*

            Configuration class for the decoding.

            Public Functions

            explicit DecodingConfig( : *std::optional<[DecodingMode](#_CPPv4N12tensorrt_llm8executor12DecodingModeE "tensorrt_llm::executor::DecodingMode")> decodingMode = std::nullopt*, : *std::optional<[LookaheadDecodingConfig](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfigE "tensorrt_llm::executor::LookaheadDecodingConfig")> lookaheadDecodingConfig = std::nullopt*, : *std::optional<[MedusaChoices](#_CPPv4N12tensorrt_llm8executor13MedusaChoicesE "tensorrt_llm::executor::MedusaChoices")> medusaChoices = std::nullopt*, : *std::optional<[EagleConfig](#_CPPv4N12tensorrt_llm8executor11EagleConfigE "tensorrt_llm::executor::EagleConfig")> eagleConfig = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor14DecodingConfig14DecodingConfigENSt8optionalI12DecodingModeEENSt8optionalI23LookaheadDecodingConfigEENSt8optionalI13MedusaChoicesEENSt8optionalI11EagleConfigEE "Link to this definition")

            bool operator==(*[DecodingConfig](#_CPPv4N12tensorrt_llm8executor14DecodingConfigE "tensorrt_llm::executor::DecodingConfig") const &other*) const[#](#_CPPv4NK12tensorrt_llm8executor14DecodingConfigeqERK14DecodingConfig "Link to this definition")

            void setDecodingMode(*[DecodingMode](#_CPPv4N12tensorrt_llm8executor12DecodingModeE "tensorrt_llm::executor::DecodingMode") const&*)[#](#_CPPv4N12tensorrt_llm8executor14DecodingConfig15setDecodingModeERK12DecodingMode "Link to this definition")
            :   Sets decoding mode. Some modes require the use of their own setters.

            std::optional<[DecodingMode](#_CPPv4N12tensorrt_llm8executor12DecodingModeE "tensorrt_llm::executor::DecodingMode")> getDecodingMode() const[#](#_CPPv4NK12tensorrt_llm8executor14DecodingConfig15getDecodingModeEv "Link to this definition")

            void setLookaheadDecodingConfig( : *[LookaheadDecodingConfig](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfigE "tensorrt_llm::executor::LookaheadDecodingConfig") const &lookaheadDecodingConfig*, )[#](#_CPPv4N12tensorrt_llm8executor14DecodingConfig26setLookaheadDecodingConfigERK23LookaheadDecodingConfig "Link to this definition")
            :   Sets lookahead decoding mode and config.

            void enableSeamlessLookaheadDecoding()[#](#_CPPv4N12tensorrt_llm8executor14DecodingConfig31enableSeamlessLookaheadDecodingEv "Link to this definition")

            std::optional<[LookaheadDecodingConfig](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfigE "tensorrt_llm::executor::LookaheadDecodingConfig")> getLookaheadDecodingConfig() const[#](#_CPPv4NK12tensorrt_llm8executor14DecodingConfig26getLookaheadDecodingConfigEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getLookaheadDecodingMaxNumRequest() const[#](#_CPPv4NK12tensorrt_llm8executor14DecodingConfig33getLookaheadDecodingMaxNumRequestEv "Link to this definition")

            void setMedusaChoices(*[MedusaChoices](#_CPPv4N12tensorrt_llm8executor13MedusaChoicesE "tensorrt_llm::executor::MedusaChoices") const&*)[#](#_CPPv4N12tensorrt_llm8executor14DecodingConfig16setMedusaChoicesERK13MedusaChoices "Link to this definition")
            :   Sets medusa mode and config.

            std::optional<[MedusaChoices](#_CPPv4N12tensorrt_llm8executor13MedusaChoicesE "tensorrt_llm::executor::MedusaChoices")> getMedusaChoices() const[#](#_CPPv4NK12tensorrt_llm8executor14DecodingConfig16getMedusaChoicesEv "Link to this definition")

            void setEagleConfig(*[EagleConfig](#_CPPv4N12tensorrt_llm8executor11EagleConfigE "tensorrt_llm::executor::EagleConfig") const&*)[#](#_CPPv4N12tensorrt_llm8executor14DecodingConfig14setEagleConfigERK11EagleConfig "Link to this definition")
            :   Sets eagle mode and config.

            std::optional<[EagleConfig](#_CPPv4N12tensorrt_llm8executor11EagleConfigE "tensorrt_llm::executor::EagleConfig")> getEagleConfig() const[#](#_CPPv4NK12tensorrt_llm8executor14DecodingConfig14getEagleConfigEv "Link to this definition")

            Private Members

            std::optional<[DecodingMode](#_CPPv4N12tensorrt_llm8executor12DecodingModeE "tensorrt_llm::executor::DecodingMode")> mDecodingMode[#](#_CPPv4N12tensorrt_llm8executor14DecodingConfig13mDecodingModeE "Link to this definition")

            std::optional<[LookaheadDecodingConfig](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfigE "tensorrt_llm::executor::LookaheadDecodingConfig")> mLookaheadDecodingConfig[#](#_CPPv4N12tensorrt_llm8executor14DecodingConfig24mLookaheadDecodingConfigE "Link to this definition")

            std::optional<[MedusaChoices](#_CPPv4N12tensorrt_llm8executor13MedusaChoicesE "tensorrt_llm::executor::MedusaChoices")> mMedusaChoices[#](#_CPPv4N12tensorrt_llm8executor14DecodingConfig14mMedusaChoicesE "Link to this definition")

            std::optional<[EagleConfig](#_CPPv4N12tensorrt_llm8executor11EagleConfigE "tensorrt_llm::executor::EagleConfig")> mEagleConfig[#](#_CPPv4N12tensorrt_llm8executor14DecodingConfig12mEagleConfigE "Link to this definition")

            Private Static Attributes

            static constexpr [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mLookaheadDecodingMaxNumRequest = 8[#](#_CPPv4N12tensorrt_llm8executor14DecodingConfig31mLookaheadDecodingMaxNumRequestE "Link to this definition")

            Friends

            *friend class* Serialization

        class DynamicBatchConfig[#](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfigE "Link to this definition")
        :   *#include <executor.h>*

            Configuration class for dynamic tuning of batch size and max num tokens. During runtime the statistics of input and output lengths are recoreded. Based on these statistics, the batch size and max num tokens are tuned dynamically to better serve the requests.

            Public Functions

            explicit DynamicBatchConfig( : *bool enableBatchSizeTuning = false*, : *bool enableMaxNumTokensTuning = false*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") dynamicBatchMovingAverageWindow = [kDefaultDynamicBatchMovingAverageWindow](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfig39kDefaultDynamicBatchMovingAverageWindowE "tensorrt_llm::executor::DynamicBatchConfig::kDefaultDynamicBatchMovingAverageWindow")*, : *std::vector<std::pair<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32"), [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> batchSizeTable = [kDefaultBatchSizeTable](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfig22kDefaultBatchSizeTableE "tensorrt_llm::executor::DynamicBatchConfig::kDefaultBatchSizeTable")*, )[#](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfig18DynamicBatchConfigEbb10SizeType32NSt6vectorINSt4pairI10SizeType3210SizeType32EEEE "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getDynamicBatchMovingAverageWindow() const[#](#_CPPv4NK12tensorrt_llm8executor18DynamicBatchConfig34getDynamicBatchMovingAverageWindowEv "Link to this definition")

            bool getEnableBatchSizeTuning() const[#](#_CPPv4NK12tensorrt_llm8executor18DynamicBatchConfig24getEnableBatchSizeTuningEv "Link to this definition")

            bool getEnableMaxNumTokensTuning() const[#](#_CPPv4NK12tensorrt_llm8executor18DynamicBatchConfig27getEnableMaxNumTokensTuningEv "Link to this definition")

            std::vector<std::pair<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32"), [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> getBatchSizeTable() const[#](#_CPPv4NK12tensorrt_llm8executor18DynamicBatchConfig17getBatchSizeTableEv "Link to this definition")

            Public Static Attributes

            static [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") const kDefaultDynamicBatchMovingAverageWindow = 128[#](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfig39kDefaultDynamicBatchMovingAverageWindowE "Link to this definition")
            :   The default window size for moving average of input and output length which is used to calculate dynamic batch size and max num tokens.

            static std::vector<std::pair<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32"), [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> const kDefaultBatchSizeTable[#](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfig22kDefaultBatchSizeTableE "Link to this definition")
            :   The default value of batch size table.

            Private Members

            bool mEnableBatchSizeTuning[#](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfig22mEnableBatchSizeTuningE "Link to this definition")
            :   Controls if the batch size should be tuned dynamically.

            bool mEnableMaxNumTokensTuning[#](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfig25mEnableMaxNumTokensTuningE "Link to this definition")
            :   Controls if the max num tokens should be tuned dynamically.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mDynamicBatchMovingAverageWindow[#](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfig32mDynamicBatchMovingAverageWindowE "Link to this definition")
            :   The window size for moving average of input and output length which is used to calculate dynamic batch size and max num tokens.

            std::vector<std::pair<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32"), [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> mBatchSizeTable[#](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfig15mBatchSizeTableE "Link to this definition")
            :   A vector of (batchSizeLimit, batchSize). When max capacity batch size is less than.

            Friends

            *friend class* Serialization

        struct EagleConfig[#](#_CPPv4N12tensorrt_llm8executor11EagleConfigE "Link to this definition")
        :   Public Functions

            explicit EagleConfig( : *std::optional<[EagleChoices](#_CPPv4N12tensorrt_llm8executor12EagleChoicesE "tensorrt_llm::executor::EagleChoices")> eagleChoices = std::nullopt*, : *bool greedySampling = true*, : *std::optional<float> posteriorThreshold = std::nullopt*, : *bool useDynamicTree = false*, : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> dynamicTreeMaxTopK = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor11EagleConfig11EagleConfigENSt8optionalI12EagleChoicesEEbNSt8optionalIfEEbNSt8optionalI10SizeType32EE "Link to this definition")

            bool operator==(*[EagleConfig](#_CPPv4N12tensorrt_llm8executor11EagleConfigE "tensorrt_llm::executor::EagleConfig") const &other*) const[#](#_CPPv4NK12tensorrt_llm8executor11EagleConfigeqERK11EagleConfig "Link to this definition")

            std::optional<[EagleChoices](#_CPPv4N12tensorrt_llm8executor12EagleChoicesE "tensorrt_llm::executor::EagleChoices")> getEagleChoices() const[#](#_CPPv4NK12tensorrt_llm8executor11EagleConfig15getEagleChoicesEv "Link to this definition")

            std::optional<float> getPosteriorThreshold() const[#](#_CPPv4NK12tensorrt_llm8executor11EagleConfig21getPosteriorThresholdEv "Link to this definition")

            bool isGreedySampling() const[#](#_CPPv4NK12tensorrt_llm8executor11EagleConfig16isGreedySamplingEv "Link to this definition")

            bool useDynamicTree() const[#](#_CPPv4NK12tensorrt_llm8executor11EagleConfig14useDynamicTreeEv "Link to this definition")

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getDynamicTreeMaxTopK() const[#](#_CPPv4NK12tensorrt_llm8executor11EagleConfig21getDynamicTreeMaxTopKEv "Link to this definition")

            Private Functions

            std::optional<float> const &checkPosteriorValue( : *std::optional<float> const &value*, )[#](#_CPPv4N12tensorrt_llm8executor11EagleConfig19checkPosteriorValueERKNSt8optionalIfEE "Link to this definition")

            Private Members

            std::optional<[EagleChoices](#_CPPv4N12tensorrt_llm8executor12EagleChoicesE "tensorrt_llm::executor::EagleChoices")> mEagleChoices[#](#_CPPv4N12tensorrt_llm8executor11EagleConfig13mEagleChoicesE "Link to this definition")
            :   choices forming tree for EAGLE-1.

            bool mGreedySampling[#](#_CPPv4N12tensorrt_llm8executor11EagleConfig15mGreedySamplingE "Link to this definition")
            :   Flag to use greedy or typical acceptance.

            std::optional<float> mPosteriorThreshold[#](#_CPPv4N12tensorrt_llm8executor11EagleConfig19mPosteriorThresholdE "Link to this definition")
            :   Minimum token probability of the typical acceptance. Corresponds to epsilon in <https://arxiv.org/pdf/2401.10774>. Default is 0.09f.

            bool mUseDynamicTree[#](#_CPPv4N12tensorrt_llm8executor11EagleConfig15mUseDynamicTreeE "Link to this definition")
            :   Flag to use Eagle-2.

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> mDynamicTreeMaxTopK[#](#_CPPv4N12tensorrt_llm8executor11EagleConfig19mDynamicTreeMaxTopKE "Link to this definition")
            :   Number of draft tokens expand for each node in Eagle-2.

            Friends

            *friend class* Serialization

        class Executor[#](#_CPPv4N12tensorrt_llm8executor8ExecutorE "Link to this definition")
        :   *#include <executor.h>*

            The executor is responsible for receiving new requests and sending responses, and running the inference.

            Public Functions

            Executor( : *std::filesystem::path const &modelPath*, : *[ModelType](#_CPPv4N12tensorrt_llm8executor9ModelTypeE "tensorrt_llm::executor::ModelType") modelType*, : *[ExecutorConfig](#_CPPv4N12tensorrt_llm8executor14ExecutorConfigE "tensorrt_llm::executor::ExecutorConfig") const &executorConfig*, )[#](#_CPPv4N12tensorrt_llm8executor8Executor8ExecutorERKNSt10filesystem4pathE9ModelTypeRK14ExecutorConfig "Link to this definition")
            :   Parameters:
                :   * **modelPath** – Path to the folder that defines the model to run
                    * **modelType** – The type of model
                    * **executorConfig** – The configuration for the executor

            Executor( : *std::filesystem::path const &encoderModelPath*, : *std::filesystem::path const &decoderModelPath*, : *[ModelType](#_CPPv4N12tensorrt_llm8executor9ModelTypeE "tensorrt_llm::executor::ModelType") modelType*, : *[ExecutorConfig](#_CPPv4N12tensorrt_llm8executor14ExecutorConfigE "tensorrt_llm::executor::ExecutorConfig") const &executorConfig*, )[#](#_CPPv4N12tensorrt_llm8executor8Executor8ExecutorERKNSt10filesystem4pathERKNSt10filesystem4pathE9ModelTypeRK14ExecutorConfig "Link to this definition")

            Executor( : *[BufferView](#_CPPv4N12tensorrt_llm8executor10BufferViewE "tensorrt_llm::executor::BufferView") const &engineBuffer*, : *std::string const &jsonConfigStr*, : *[ModelType](#_CPPv4N12tensorrt_llm8executor9ModelTypeE "tensorrt_llm::executor::ModelType") modelType*, : *[ExecutorConfig](#_CPPv4N12tensorrt_llm8executor14ExecutorConfigE "tensorrt_llm::executor::ExecutorConfig") const &executorConfig*, : *std::optional<std::map<std::string, [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")>> const &managedWeights = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor8Executor8ExecutorERK10BufferViewRKNSt6stringE9ModelTypeRK14ExecutorConfigRKNSt8optionalINSt3mapINSt6stringE6TensorEEEE "Link to this definition")

            Executor( : *[BufferView](#_CPPv4N12tensorrt_llm8executor10BufferViewE "tensorrt_llm::executor::BufferView") const &encoderEngineBuffer*, : *std::string const &encoderJsonConfigStr*, : *[BufferView](#_CPPv4N12tensorrt_llm8executor10BufferViewE "tensorrt_llm::executor::BufferView") const &decoderEngineBuffer*, : *std::string const &decoderJsonConfigStr*, : *[ModelType](#_CPPv4N12tensorrt_llm8executor9ModelTypeE "tensorrt_llm::executor::ModelType") modelType*, : *[ExecutorConfig](#_CPPv4N12tensorrt_llm8executor14ExecutorConfigE "tensorrt_llm::executor::ExecutorConfig") const &executorConfig*, )[#](#_CPPv4N12tensorrt_llm8executor8Executor8ExecutorERK10BufferViewRKNSt6stringERK10BufferViewRKNSt6stringE9ModelTypeRK14ExecutorConfig "Link to this definition")

            Executor( : *std::shared\_ptr<Model> model*, : *[ExecutorConfig](#_CPPv4N12tensorrt_llm8executor14ExecutorConfigE "tensorrt_llm::executor::ExecutorConfig") const &executorConfig*, )[#](#_CPPv4N12tensorrt_llm8executor8Executor8ExecutorENSt10shared_ptrI5ModelEERK14ExecutorConfig "Link to this definition")

            Executor( : *std::shared\_ptr<Model> encoderModel*, : *std::shared\_ptr<Model> decoderModel*, : *[ExecutorConfig](#_CPPv4N12tensorrt_llm8executor14ExecutorConfigE "tensorrt_llm::executor::ExecutorConfig") const &executorConfig*, )[#](#_CPPv4N12tensorrt_llm8executor8Executor8ExecutorENSt10shared_ptrI5ModelEENSt10shared_ptrI5ModelEERK14ExecutorConfig "Link to this definition")

            ~Executor()[#](#_CPPv4N12tensorrt_llm8executor8ExecutorD0Ev "Link to this definition")

            Executor(*[Executor](#_CPPv4N12tensorrt_llm8executor8Executor8ExecutorERK8Executor "tensorrt_llm::executor::Executor::Executor") const &executor*) = delete[#](#_CPPv4N12tensorrt_llm8executor8Executor8ExecutorERK8Executor "Link to this definition")

            [Executor](#_CPPv4N12tensorrt_llm8executor8ExecutorE "tensorrt_llm::executor::Executor") &operator=(*[Executor](#_CPPv4N12tensorrt_llm8executor8ExecutorE "tensorrt_llm::executor::Executor") const &executor*) = delete[#](#_CPPv4N12tensorrt_llm8executor8ExecutoraSERK8Executor "Link to this definition")

            Executor(*[Executor](#_CPPv4N12tensorrt_llm8executor8Executor8ExecutorERR8Executor "tensorrt_llm::executor::Executor::Executor")&&*) = default[#](#_CPPv4N12tensorrt_llm8executor8Executor8ExecutorERR8Executor "Link to this definition")

            [Executor](#_CPPv4N12tensorrt_llm8executor8ExecutorE "tensorrt_llm::executor::Executor") &operator=(*[Executor](#_CPPv4N12tensorrt_llm8executor8ExecutorE "tensorrt_llm::executor::Executor")&&*) = default[#](#_CPPv4N12tensorrt_llm8executor8ExecutoraSERR8Executor "Link to this definition")

            [IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") enqueueRequest(*[Request](#_CPPv4N12tensorrt_llm8executor7RequestE "tensorrt_llm::executor::Request") const &request*)[#](#_CPPv4N12tensorrt_llm8executor8Executor14enqueueRequestERK7Request "Link to this definition")
            :   Enqueue a new request.

                Parameters:
                :   **request** – The LLM request which contains input tokens and request parameters

                Returns:
                :   A unique id that identifies the request

            std::vector<[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType")> enqueueRequests( : *std::vector<[Request](#_CPPv4N12tensorrt_llm8executor7RequestE "tensorrt_llm::executor::Request")> const &requests*, )[#](#_CPPv4N12tensorrt_llm8executor8Executor15enqueueRequestsERKNSt6vectorI7RequestEE "Link to this definition")
            :   Enqueue a batch of request.

            std::vector<[Response](#_CPPv4N12tensorrt_llm8executor8ResponseE "tensorrt_llm::executor::Response")> awaitResponses( : *std::optional<std::chrono::milliseconds> const &timeout = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor8Executor14awaitResponsesERKNSt8optionalINSt6chrono12millisecondsEEE "Link to this definition")
            :   Await for ready responses.

                ```
                   This overload awaits for any ready responses. In particular, if several requests
                   have been enqueued, this method will provide any ready responses without order guarantees.
                ```

                Parameters:
                :   **timeout** – The maximum time to wait for new responses

                Returns:
                :   A vector of responses

            std::vector<[Response](#_CPPv4N12tensorrt_llm8executor8ResponseE "tensorrt_llm::executor::Response")> awaitResponses( : *[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") const &requestId*, : *std::optional<std::chrono::milliseconds> const &timeout = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor8Executor14awaitResponsesERK6IdTypeRKNSt8optionalINSt6chrono12millisecondsEEE "Link to this definition")
            :   Await for ready responses.

                Parameters:
                :   * **id** – A request id
                    * **timeout** – The maximum time to wait for new responses

                Returns:
                :   A vector of responses

            std::vector<std::vector<[Response](#_CPPv4N12tensorrt_llm8executor8ResponseE "tensorrt_llm::executor::Response")>> awaitResponses( : *std::vector<[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType")> const &requestIds*, : *std::optional<std::chrono::milliseconds> const &timeout = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor8Executor14awaitResponsesERKNSt6vectorI6IdTypeEERKNSt8optionalINSt6chrono12millisecondsEEE "Link to this definition")
            :   Await for multiple ready responses.

                ```
                   A multiple ID request behaves as if awaitResponses(IdType, timeout)
                   were invoked on all IDs. The returned vector contains
                   a vector of responses per ID in the same order specified by the requestIds.
                   The same behaviour as awaitResponses(IdType, timeout) applies:
                   * Responses may be empty.
                   * If all responses have already been given for one of the requestIds,
                     then this method will hang unless a timeout is specified.
                ```

                Parameters:
                :   * **requestIds** – Ids requested
                    * **timeout** – The maximum time to wait for new responses

                Returns:
                :   A vector of vector of responses

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getNumResponsesReady( : *std::optional<[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType")> const &requestId = std::nullopt*, ) const[#](#_CPPv4NK12tensorrt_llm8executor8Executor20getNumResponsesReadyERKNSt8optionalI6IdTypeEE "Link to this definition")
            :   Get the number of ready responses.

                Parameters:
                :   **requestId** – An optional request id

                Returns:
                :   The number of ready responses

            void cancelRequest(*[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") requestId*)[#](#_CPPv4N12tensorrt_llm8executor8Executor13cancelRequestE6IdType "Link to this definition")
            :   Cancel the request with provided request id.

                Parameters:
                :   **id** – The request id for which to cancel the response

            void shutdown()[#](#_CPPv4N12tensorrt_llm8executor8Executor8shutdownEv "Link to this definition")
            :   Signals the server to shutdown.

                This call is blocking. Only returns when all requests have terminated or timeout has been reached

            std::deque<[IterationStats](#_CPPv4N12tensorrt_llm8executor14IterationStatsE "tensorrt_llm::executor::IterationStats")> getLatestIterationStats()[#](#_CPPv4N12tensorrt_llm8executor8Executor23getLatestIterationStatsEv "Link to this definition")
            :   Returns the per-iterations statistics computed since last call to getLatestIterationStats. Contains at most iterStatsMaxIterations iterations.

                Returns:
                :   Iteration stats

            std::deque<[RequestStatsPerIteration](#_CPPv4N12tensorrt_llm8executor24RequestStatsPerIterationE "tensorrt_llm::executor::RequestStatsPerIteration")> getLatestRequestStats()[#](#_CPPv4N12tensorrt_llm8executor8Executor21getLatestRequestStatsEv "Link to this definition")
            :   Returns the request stats of each iteration computed since last call to getLatestRequestStats. Contains at most requestStatsMaxIterations iterations.

                Returns:
                :   [Request](#classtensorrt__llm_1_1executor_1_1Request) stats grouped by iterations

            std::deque<[DebugTensorsPerIteration](#_CPPv4N12tensorrt_llm8executor24DebugTensorsPerIterationE "tensorrt_llm::executor::DebugTensorsPerIteration")> getLatestDebugTensors()[#](#_CPPv4N12tensorrt_llm8executor8Executor21getLatestDebugTensorsEv "Link to this definition")
            :   Returns the debug tensors of each iteration computed since last call to getLatestDebugTensors. Contains at most debugTensorsMaxIterations iterations.

                Returns:
                :   [Request](#classtensorrt__llm_1_1executor_1_1Request) debug tensors grouped by iterations

            bool canEnqueueRequests() const[#](#_CPPv4NK12tensorrt_llm8executor8Executor18canEnqueueRequestsEv "Link to this definition")
            :   Indicates if the current process is allowed to enqueueRequests.

            bool isParticipant() const[#](#_CPPv4NK12tensorrt_llm8executor8Executor13isParticipantEv "Link to this definition")
            :   Indicates if the current process participates in this executor instance.

            std::optional<std::shared\_ptr<[KVCacheEventManager](#_CPPv4N12tensorrt_llm8executor19KVCacheEventManagerE "tensorrt_llm::executor::KVCacheEventManager")>> getKVCacheEventManager() const[#](#_CPPv4NK12tensorrt_llm8executor8Executor22getKVCacheEventManagerEv "Link to this definition")

            Private Members

            std::unique\_ptr<Impl> mImpl[#](#_CPPv4N12tensorrt_llm8executor8Executor5mImplE "Link to this definition")

        class ExecutorConfig[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfigE "Link to this definition")
        :   *#include <executor.h>*

            Configuration class for the model executor.

            Public Functions

            explicit ExecutorConfig( : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") maxBeamWidth = 1*, : *[SchedulerConfig](#_CPPv4N12tensorrt_llm8executor15SchedulerConfigE "tensorrt_llm::executor::SchedulerConfig") schedulerConfig = [SchedulerConfig](#_CPPv4N12tensorrt_llm8executor15SchedulerConfigE "tensorrt_llm::executor::SchedulerConfig")()*, : *[KvCacheConfig](#_CPPv4N12tensorrt_llm8executor13KvCacheConfigE "tensorrt_llm::executor::KvCacheConfig") kvCacheConfig = [KvCacheConfig](#_CPPv4N12tensorrt_llm8executor13KvCacheConfigE "tensorrt_llm::executor::KvCacheConfig")()*, : *bool enableChunkedContext = true*, : *bool normalizeLogProbs = true*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") iterStatsMaxIterations = [kDefaultIterStatsMaxIterations](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig30kDefaultIterStatsMaxIterationsE "tensorrt_llm::executor::ExecutorConfig::kDefaultIterStatsMaxIterations")*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") requestStatsMaxIterations = [kDefaultRequestStatsMaxIterations](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig33kDefaultRequestStatsMaxIterationsE "tensorrt_llm::executor::ExecutorConfig::kDefaultRequestStatsMaxIterations")*, : *[BatchingType](#_CPPv4N12tensorrt_llm8executor12BatchingTypeE "tensorrt_llm::executor::BatchingType") batchingType = [BatchingType](#_CPPv4N12tensorrt_llm8executor12BatchingTypeE "tensorrt_llm::executor::BatchingType")::[kINFLIGHT](#_CPPv4N12tensorrt_llm8executor12BatchingType9kINFLIGHTE "tensorrt_llm::executor::BatchingType::kINFLIGHT")*, : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> maxBatchSize = std::nullopt*, : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> maxNumTokens = std::nullopt*, : *std::optional<[ParallelConfig](#_CPPv4N12tensorrt_llm8executor14ParallelConfigE "tensorrt_llm::executor::ParallelConfig")> parallelConfig = std::nullopt*, : *std::optional<[PeftCacheConfig](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfigE "tensorrt_llm::executor::PeftCacheConfig")> const &peftCacheConfig = std::nullopt*, : *std::optional<[LogitsPostProcessorConfig](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfigE "tensorrt_llm::executor::LogitsPostProcessorConfig")> logitsPostProcessorConfig = std::nullopt*, : *std::optional<[DecodingConfig](#_CPPv4N12tensorrt_llm8executor14DecodingConfigE "tensorrt_llm::executor::DecodingConfig")> decodingConfig = std::nullopt*, : *bool useGpuDirectStorage = false*, : *float gpuWeightsPercent = 1*, : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> maxQueueSize = std::nullopt*, : *[ExtendedRuntimePerfKnobConfig](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfigE "tensorrt_llm::executor::ExtendedRuntimePerfKnobConfig") const &extendedRuntimePerfKnobConfig = [ExtendedRuntimePerfKnobConfig](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfigE "tensorrt_llm::executor::ExtendedRuntimePerfKnobConfig")()*, : *std::optional<[DebugConfig](#_CPPv4N12tensorrt_llm8executor11DebugConfigE "tensorrt_llm::executor::DebugConfig")> debugConfig = std::nullopt*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") recvPollPeriodMs = 0*, : *uint64\_t maxSeqIdleMicroseconds = [kDefaultMaxSeqIdleMicroseconds](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig30kDefaultMaxSeqIdleMicrosecondsE "tensorrt_llm::executor::ExecutorConfig::kDefaultMaxSeqIdleMicroseconds")*, : *std::optional<[SpeculativeDecodingConfig](#_CPPv4N12tensorrt_llm8executor25SpeculativeDecodingConfigE "tensorrt_llm::executor::SpeculativeDecodingConfig")> specDecConfig = std::nullopt*, : *std::optional<[GuidedDecodingConfig](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfigE "tensorrt_llm::executor::GuidedDecodingConfig")> guidedDecodingConfig = std::nullopt*, : *std::optional<std::vector<[AdditionalModelOutput](#_CPPv4N12tensorrt_llm8executor21AdditionalModelOutputE "tensorrt_llm::executor::AdditionalModelOutput")>> additionalModelOutputs = std::nullopt*, : *std::optional<[CacheTransceiverConfig](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfigE "tensorrt_llm::executor::CacheTransceiverConfig")> cacheTransceiverConfig = std::nullopt*, : *bool gatherGenerationLogits = false*, : *bool promptTableOffloading = false*, : *bool enableTrtOverlap = false*, : *bool failFastOnAttentionWindowTooLarge = false*, )[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig14ExecutorConfigE10SizeType3215SchedulerConfig13KvCacheConfigbb10SizeType3210SizeType3212BatchingTypeNSt8optionalI10SizeType32EENSt8optionalI10SizeType32EENSt8optionalI14ParallelConfigEERKNSt8optionalI15PeftCacheConfigEENSt8optionalI25LogitsPostProcessorConfigEENSt8optionalI14DecodingConfigEEbfNSt8optionalI10SizeType32EERK29ExtendedRuntimePerfKnobConfigNSt8optionalI11DebugConfigEE10SizeType328uint64_tNSt8optionalI25SpeculativeDecodingConfigEENSt8optionalI20GuidedDecodingConfigEENSt8optionalINSt6vectorI21AdditionalModelOutputEEEENSt8optionalI22CacheTransceiverConfigEEbbbb "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getMaxBeamWidth() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig15getMaxBeamWidthEv "Link to this definition")

            [SchedulerConfig](#_CPPv4N12tensorrt_llm8executor15SchedulerConfigE "tensorrt_llm::executor::SchedulerConfig") getSchedulerConfig() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig18getSchedulerConfigEv "Link to this definition")

            [KvCacheConfig](#_CPPv4N12tensorrt_llm8executor13KvCacheConfigE "tensorrt_llm::executor::KvCacheConfig") getKvCacheConfig() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig16getKvCacheConfigEv "Link to this definition")

            [SchedulerConfig](#_CPPv4N12tensorrt_llm8executor15SchedulerConfigE "tensorrt_llm::executor::SchedulerConfig") &getSchedulerConfigRef()[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig21getSchedulerConfigRefEv "Link to this definition")

            [KvCacheConfig](#_CPPv4N12tensorrt_llm8executor13KvCacheConfigE "tensorrt_llm::executor::KvCacheConfig") &getKvCacheConfigRef()[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig19getKvCacheConfigRefEv "Link to this definition")

            bool getEnableChunkedContext() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig23getEnableChunkedContextEv "Link to this definition")

            bool getNormalizeLogProbs() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig20getNormalizeLogProbsEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getIterStatsMaxIterations() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig25getIterStatsMaxIterationsEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getRequestStatsMaxIterations() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig28getRequestStatsMaxIterationsEv "Link to this definition")

            [BatchingType](#_CPPv4N12tensorrt_llm8executor12BatchingTypeE "tensorrt_llm::executor::BatchingType") getBatchingType() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig15getBatchingTypeEv "Link to this definition")

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getMaxBatchSize() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig15getMaxBatchSizeEv "Link to this definition")

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getMaxNumTokens() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig15getMaxNumTokensEv "Link to this definition")

            std::optional<[ParallelConfig](#_CPPv4N12tensorrt_llm8executor14ParallelConfigE "tensorrt_llm::executor::ParallelConfig")> getParallelConfig() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig17getParallelConfigEv "Link to this definition")

            std::optional<[PeftCacheConfig](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfigE "tensorrt_llm::executor::PeftCacheConfig")> getPeftCacheConfig() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig18getPeftCacheConfigEv "Link to this definition")

            std::optional<[LogitsPostProcessorConfig](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfigE "tensorrt_llm::executor::LogitsPostProcessorConfig")> getLogitsPostProcessorConfig() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig28getLogitsPostProcessorConfigEv "Link to this definition")

            std::optional<[DecodingConfig](#_CPPv4N12tensorrt_llm8executor14DecodingConfigE "tensorrt_llm::executor::DecodingConfig")> getDecodingConfig() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig17getDecodingConfigEv "Link to this definition")

            bool getUseGpuDirectStorage() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig22getUseGpuDirectStorageEv "Link to this definition")

            float getGpuWeightsPercent() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig20getGpuWeightsPercentEv "Link to this definition")

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getMaxQueueSize() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig15getMaxQueueSizeEv "Link to this definition")

            [ExtendedRuntimePerfKnobConfig](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfigE "tensorrt_llm::executor::ExtendedRuntimePerfKnobConfig") getExtendedRuntimePerfKnobConfig() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig32getExtendedRuntimePerfKnobConfigEv "Link to this definition")

            std::optional<[DebugConfig](#_CPPv4N12tensorrt_llm8executor11DebugConfigE "tensorrt_llm::executor::DebugConfig")> getDebugConfig() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig14getDebugConfigEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getRecvPollPeriodMs() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig19getRecvPollPeriodMsEv "Link to this definition")

            uint64\_t getMaxSeqIdleMicroseconds() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig25getMaxSeqIdleMicrosecondsEv "Link to this definition")

            std::optional<[SpeculativeDecodingConfig](#_CPPv4N12tensorrt_llm8executor25SpeculativeDecodingConfigE "tensorrt_llm::executor::SpeculativeDecodingConfig")> getSpecDecConfig() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig16getSpecDecConfigEv "Link to this definition")

            std::optional<[GuidedDecodingConfig](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfigE "tensorrt_llm::executor::GuidedDecodingConfig")> getGuidedDecodingConfig() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig23getGuidedDecodingConfigEv "Link to this definition")

            std::optional<std::vector<[AdditionalModelOutput](#_CPPv4N12tensorrt_llm8executor21AdditionalModelOutputE "tensorrt_llm::executor::AdditionalModelOutput")>> getAdditionalModelOutputs() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig25getAdditionalModelOutputsEv "Link to this definition")

            bool getGatherGenerationLogits() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig25getGatherGenerationLogitsEv "Link to this definition")

            bool getPromptTableOffloading() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig24getPromptTableOffloadingEv "Link to this definition")

            std::optional<[CacheTransceiverConfig](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfigE "tensorrt_llm::executor::CacheTransceiverConfig")> getCacheTransceiverConfig() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig25getCacheTransceiverConfigEv "Link to this definition")

            bool getEnableTrtOverlap() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig19getEnableTrtOverlapEv "Link to this definition")

            bool getFailFastOnAttentionWindowTooLarge() const[#](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig36getFailFastOnAttentionWindowTooLargeEv "Link to this definition")

            void setMaxBeamWidth(*[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") maxBeamWidth*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig15setMaxBeamWidthE10SizeType32 "Link to this definition")

            void setMaxBatchSize(*[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") maxBatchSize*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig15setMaxBatchSizeE10SizeType32 "Link to this definition")

            void setMaxNumTokens(*[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") maxNumTokens*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig15setMaxNumTokensE10SizeType32 "Link to this definition")

            void setSchedulerConfig(*[SchedulerConfig](#_CPPv4N12tensorrt_llm8executor15SchedulerConfigE "tensorrt_llm::executor::SchedulerConfig") const &schedulerConfig*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig18setSchedulerConfigERK15SchedulerConfig "Link to this definition")

            void setKvCacheConfig(*[KvCacheConfig](#_CPPv4N12tensorrt_llm8executor13KvCacheConfigE "tensorrt_llm::executor::KvCacheConfig") const &kvCacheConfig*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig16setKvCacheConfigERK13KvCacheConfig "Link to this definition")

            void setEnableChunkedContext(*bool enableChunkedContext*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig23setEnableChunkedContextEb "Link to this definition")

            void setNormalizeLogProbs(*bool normalizeLogProbs*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig20setNormalizeLogProbsEb "Link to this definition")

            void setIterStatsMaxIterations(*[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") iterStatsMaxIterations*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig25setIterStatsMaxIterationsE10SizeType32 "Link to this definition")

            void setRequestStatsMaxIterations( : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") requestStatsMaxIterations*, )[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig28setRequestStatsMaxIterationsE10SizeType32 "Link to this definition")

            void setBatchingType(*[BatchingType](#_CPPv4N12tensorrt_llm8executor12BatchingTypeE "tensorrt_llm::executor::BatchingType") batchingType*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig15setBatchingTypeE12BatchingType "Link to this definition")

            void setParallelConfig(*[ParallelConfig](#_CPPv4N12tensorrt_llm8executor14ParallelConfigE "tensorrt_llm::executor::ParallelConfig") const &parallelConfig*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig17setParallelConfigERK14ParallelConfig "Link to this definition")

            void setPeftCacheConfig(*[PeftCacheConfig](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfigE "tensorrt_llm::executor::PeftCacheConfig") const &peftCacheConfig*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig18setPeftCacheConfigERK15PeftCacheConfig "Link to this definition")

            void setLogitsPostProcessorConfig( : *[LogitsPostProcessorConfig](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfigE "tensorrt_llm::executor::LogitsPostProcessorConfig") const &logitsPostProcessorConfig*, )[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig28setLogitsPostProcessorConfigERK25LogitsPostProcessorConfig "Link to this definition")

            void setDecodingConfig(*[DecodingConfig](#_CPPv4N12tensorrt_llm8executor14DecodingConfigE "tensorrt_llm::executor::DecodingConfig") const &decodingConfig*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig17setDecodingConfigERK14DecodingConfig "Link to this definition")

            void setUseGpuDirectStorage(*bool const &useGpuDirectStorage*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig22setUseGpuDirectStorageERKb "Link to this definition")

            void setGpuWeightsPercent(*float const &gpuWeightsPercent*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig20setGpuWeightsPercentERKf "Link to this definition")

            void setMaxQueueSize(*std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &maxQueueSize*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig15setMaxQueueSizeERKNSt8optionalI10SizeType32EE "Link to this definition")

            void setExtendedRuntimePerfKnobConfig( : *[ExtendedRuntimePerfKnobConfig](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfigE "tensorrt_llm::executor::ExtendedRuntimePerfKnobConfig") const &extendedRuntimePerfKnobConfig*, )[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig32setExtendedRuntimePerfKnobConfigERK29ExtendedRuntimePerfKnobConfig "Link to this definition")

            void setDebugConfig(*[DebugConfig](#_CPPv4N12tensorrt_llm8executor11DebugConfigE "tensorrt_llm::executor::DebugConfig") const &debugConfig*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig14setDebugConfigERK11DebugConfig "Link to this definition")

            void setRecvPollPeriodMs(*[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") const &recvPollPeriodMs*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig19setRecvPollPeriodMsERK10SizeType32 "Link to this definition")

            void setMaxSeqIdleMicroseconds(*uint64\_t maxSeqIdleMicroseconds*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig25setMaxSeqIdleMicrosecondsE8uint64_t "Link to this definition")

            void setSpecDecConfig(*[SpeculativeDecodingConfig](#_CPPv4N12tensorrt_llm8executor25SpeculativeDecodingConfigE "tensorrt_llm::executor::SpeculativeDecodingConfig") const &specDecConfig*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig16setSpecDecConfigERK25SpeculativeDecodingConfig "Link to this definition")

            void setGuidedDecodingConfig( : *[GuidedDecodingConfig](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfigE "tensorrt_llm::executor::GuidedDecodingConfig") const &guidedDecodingConfig*, )[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig23setGuidedDecodingConfigERK20GuidedDecodingConfig "Link to this definition")

            void setAdditionalModelOutputs( : *std::vector<[AdditionalModelOutput](#_CPPv4N12tensorrt_llm8executor21AdditionalModelOutputE "tensorrt_llm::executor::AdditionalModelOutput")> const &additionalModelOutputs*, )[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig25setAdditionalModelOutputsERKNSt6vectorI21AdditionalModelOutputEE "Link to this definition")

            void setGatherGenerationLogits(*bool gatherGenerationLogits*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig25setGatherGenerationLogitsEb "Link to this definition")

            void setPromptTableOffloading(*bool promptTableOffloading*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig24setPromptTableOffloadingEb "Link to this definition")

            void setCacheTransceiverConfig( : *[CacheTransceiverConfig](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfigE "tensorrt_llm::executor::CacheTransceiverConfig") const &cacheTransceiverConfig*, )[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig25setCacheTransceiverConfigERK22CacheTransceiverConfig "Link to this definition")

            void setEnableTrtOverlap(*bool enableTrtOverlap*)[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig19setEnableTrtOverlapEb "Link to this definition")

            void setFailFastOnAttentionWindowTooLarge( : *bool failFastOnAttentionWindowTooLarge*, )[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig36setFailFastOnAttentionWindowTooLargeEb "Link to this definition")

            Public Static Attributes

            static constexpr uint64\_t kDefaultMaxSeqIdleMicroseconds = 180000000[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig30kDefaultMaxSeqIdleMicrosecondsE "Link to this definition")

            static constexpr [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") kDefaultIterStatsMaxIterations = 1000[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig30kDefaultIterStatsMaxIterationsE "Link to this definition")

            static constexpr [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") kDefaultRequestStatsMaxIterations = 0[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig33kDefaultRequestStatsMaxIterationsE "Link to this definition")

            Private Members

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mMaxBeamWidth[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig13mMaxBeamWidthE "Link to this definition")
            :   The beam width value of requests that will be sent to the executor.

            [SchedulerConfig](#_CPPv4N12tensorrt_llm8executor15SchedulerConfigE "tensorrt_llm::executor::SchedulerConfig") mSchedulerConfig[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig16mSchedulerConfigE "Link to this definition")
            :   The scheduler configuration.

            [KvCacheConfig](#_CPPv4N12tensorrt_llm8executor13KvCacheConfigE "tensorrt_llm::executor::KvCacheConfig") mKvCacheConfig[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig14mKvCacheConfigE "Link to this definition")
            :   The KV cache configuration.

            bool mEnableChunkedContext[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig21mEnableChunkedContextE "Link to this definition")
            :   Controls whether context is allowed to be chunked.

            bool mNormalizeLogProbs[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig18mNormalizeLogProbsE "Link to this definition")
            :   Controls if log probabilities should be normalized or not.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mIterStatsMaxIterations[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig23mIterStatsMaxIterationsE "Link to this definition")
            :   Controls the maximum number of iterations for which to keep statistics.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mRequestStatsMaxIterations[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig26mRequestStatsMaxIterationsE "Link to this definition")
            :   Controls the maximum number of iterations for which to keep per-request statistics.

            [BatchingType](#_CPPv4N12tensorrt_llm8executor12BatchingTypeE "tensorrt_llm::executor::BatchingType") mBatchingType[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig13mBatchingTypeE "Link to this definition")
            :   The type of batching strategy to use. See BatchingType.

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> mMaxBatchSize[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig13mMaxBatchSizeE "Link to this definition")
            :   The max batch size of requests.

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> mMaxNumTokens[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig13mMaxNumTokensE "Link to this definition")
            :   The max number of tokens per batch.

            std::optional<[ParallelConfig](#_CPPv4N12tensorrt_llm8executor14ParallelConfigE "tensorrt_llm::executor::ParallelConfig")> mParallelConfig[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig15mParallelConfigE "Link to this definition")
            :   The parallel execution configuration.

            std::optional<[PeftCacheConfig](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfigE "tensorrt_llm::executor::PeftCacheConfig")> mPeftCacheConfig[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig16mPeftCacheConfigE "Link to this definition")

            std::optional<[LogitsPostProcessorConfig](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfigE "tensorrt_llm::executor::LogitsPostProcessorConfig")> mLogitsPostProcessorConfig[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig26mLogitsPostProcessorConfigE "Link to this definition")
            :   Logits post processor configuration.

            std::optional<[DecodingConfig](#_CPPv4N12tensorrt_llm8executor14DecodingConfigE "tensorrt_llm::executor::DecodingConfig")> mDecodingConfig[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig15mDecodingConfigE "Link to this definition")
            :   Decoding configuration.

            bool mUseGpuDirectStorage[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig20mUseGpuDirectStorageE "Link to this definition")
            :   Enable/disable use of GPU Direct Storage (GDS) to load engines.

            float mGpuWeightsPercent[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig18mGpuWeightsPercentE "Link to this definition")
            :   GPU weights percent for weight streaming.

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> mMaxQueueSize[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig13mMaxQueueSizeE "Link to this definition")
            :   The maximum number of requests allowed in queue before rejecting new requests.

            [ExtendedRuntimePerfKnobConfig](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfigE "tensorrt_llm::executor::ExtendedRuntimePerfKnobConfig") mExtendedRuntimePerfKnobConfig[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig30mExtendedRuntimePerfKnobConfigE "Link to this definition")
            :   Config for perf knobs that can be set in runtime.

            std::optional<[DebugConfig](#_CPPv4N12tensorrt_llm8executor11DebugConfigE "tensorrt_llm::executor::DebugConfig")> mDebugConfig[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig12mDebugConfigE "Link to this definition")
            :   Debugging configuration.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mRecvPollPeriodMs[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig17mRecvPollPeriodMsE "Link to this definition")
            :   The time in ms between polls for new communication in orchestrator mode. Use 0 for busy loop.

            uint64\_t mMaxSeqIdleMicroseconds[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig23mMaxSeqIdleMicrosecondsE "Link to this definition")
            :   The maximum time in microseconds a scheduled request can remain idle before getting terminated. Default value is 3 minutes.

            std::optional<[SpeculativeDecodingConfig](#_CPPv4N12tensorrt_llm8executor25SpeculativeDecodingConfigE "tensorrt_llm::executor::SpeculativeDecodingConfig")> mSpeculativeDecodingConfig[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig26mSpeculativeDecodingConfigE "Link to this definition")
            :   The speculative decoding configuration.

            std::optional<[GuidedDecodingConfig](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfigE "tensorrt_llm::executor::GuidedDecodingConfig")> mGuidedDecodingConfig[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig21mGuidedDecodingConfigE "Link to this definition")
            :   The guided decoding configuration.

            std::optional<std::vector<[AdditionalModelOutput](#_CPPv4N12tensorrt_llm8executor21AdditionalModelOutputE "tensorrt_llm::executor::AdditionalModelOutput")>> mAdditionalModelOutputs[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig23mAdditionalModelOutputsE "Link to this definition")
            :   The additional outputs to gather from the model.

            std::optional<[CacheTransceiverConfig](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfigE "tensorrt_llm::executor::CacheTransceiverConfig")> mCacheTransceiverConfig[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig23mCacheTransceiverConfigE "Link to this definition")
            :   The cache transceiver configuration.

            bool mGatherGenerationLogits = {false}[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig23mGatherGenerationLogitsE "Link to this definition")
            :   Controls if generation logits should be gathered, so that returnGenerationLogits can be requested.

            bool mPromptTableOffloading = {false}[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig22mPromptTableOffloadingE "Link to this definition")
            :   Controls if prompt table offloading is enabled.

            bool mEnableTrtOverlap = {false}[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig17mEnableTrtOverlapE "Link to this definition")
            :   Controls whether preparation and TRT engine execution should be overlapped.

            bool mFailFastOnAttentionWindowTooLarge = {false}[#](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig34mFailFastOnAttentionWindowTooLargeE "Link to this definition")
            :   Controls whether to fail fast when attention window is too large to fit even a single sequence in the KV cache.

            Friends

            *friend class* Serialization

        class ExtendedRuntimePerfKnobConfig[#](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfigE "Link to this definition")
        :   *#include <executor.h>*

            Configuration class for the runtime perf knobs.

            Public Functions

            explicit ExtendedRuntimePerfKnobConfig( : *bool multiBlockMode = true*, : *bool enableContextFMHAFP32Acc = false*, : *bool cudaGraphMode = false*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") cudaGraphCacheSize = 0*, )[#](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig29ExtendedRuntimePerfKnobConfigEbbb10SizeType32 "Link to this definition")

            inline bool operator==( : *[ExtendedRuntimePerfKnobConfig](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfigE "tensorrt_llm::executor::ExtendedRuntimePerfKnobConfig") const &other*, ) const[#](#_CPPv4NK12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfigeqERK29ExtendedRuntimePerfKnobConfig "Link to this definition")

            bool getMultiBlockMode() const[#](#_CPPv4NK12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig17getMultiBlockModeEv "Link to this definition")

            bool getEnableContextFMHAFP32Acc() const[#](#_CPPv4NK12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig27getEnableContextFMHAFP32AccEv "Link to this definition")

            bool getCudaGraphMode() const[#](#_CPPv4NK12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig16getCudaGraphModeEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getCudaGraphCacheSize() const[#](#_CPPv4NK12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig21getCudaGraphCacheSizeEv "Link to this definition")

            void setMultiBlockMode(*bool multiBlockMode*)[#](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig17setMultiBlockModeEb "Link to this definition")

            void setEnableContextFMHAFP32Acc(*bool enableContextFMHAFP32Acc*)[#](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig27setEnableContextFMHAFP32AccEb "Link to this definition")

            void setCudaGraphMode(*bool cudaGraphMode*)[#](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig16setCudaGraphModeEb "Link to this definition")

            void setCudaGraphCacheSize(*[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") cacheSize*)[#](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig21setCudaGraphCacheSizeE10SizeType32 "Link to this definition")

            Private Members

            bool mMultiBlockMode[#](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig15mMultiBlockModeE "Link to this definition")
            :   Control if multi block mode should be enabled or not.

            bool mEnableContextFMHAFP32Acc[#](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig25mEnableContextFMHAFP32AccE "Link to this definition")
            :   If enable FMHA runner FP32 accumulation.

            bool mCudaGraphMode[#](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig14mCudaGraphModeE "Link to this definition")
            :   Control if enable cuda graph.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mCudaGraphCacheSize[#](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig19mCudaGraphCacheSizeE "Link to this definition")
            :   Number of cuda graphs to be cached in the runtime. The larger the cache, the better the perf, but more GPU memory is consumed.

            Friends

            *friend class* Serialization

        class ExternalDraftTokensConfig[#](#_CPPv4N12tensorrt_llm8executor25ExternalDraftTokensConfigE "Link to this definition")
        :   *#include <executor.h>*

            Configuration for speculative decoding with external draft tokens. Allows to include draft tokens, draft logits and specify acceptance threshold.

            Public Functions

            explicit ExternalDraftTokensConfig( : *[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens") tokens*, : *std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> logits = std::nullopt*, : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &acceptanceThreshold = std::nullopt*, : *std::optional<bool> const &fastLogits = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor25ExternalDraftTokensConfig25ExternalDraftTokensConfigE9VecTokensNSt8optionalI6TensorEERKNSt8optionalI9FloatTypeEERKNSt8optionalIbEE "Link to this definition")

            [VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens") getTokens() const[#](#_CPPv4NK12tensorrt_llm8executor25ExternalDraftTokensConfig9getTokensEv "Link to this definition")

            std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> getLogits() const[#](#_CPPv4NK12tensorrt_llm8executor25ExternalDraftTokensConfig9getLogitsEv "Link to this definition")

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> getAcceptanceThreshold() const[#](#_CPPv4NK12tensorrt_llm8executor25ExternalDraftTokensConfig22getAcceptanceThresholdEv "Link to this definition")

            std::optional<bool> getFastLogits() const[#](#_CPPv4NK12tensorrt_llm8executor25ExternalDraftTokensConfig13getFastLogitsEv "Link to this definition")

            Private Members

            [VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens") mTokens[#](#_CPPv4N12tensorrt_llm8executor25ExternalDraftTokensConfig7mTokensE "Link to this definition")
            :   The draft tokens.

            std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> mLogits[#](#_CPPv4N12tensorrt_llm8executor25ExternalDraftTokensConfig7mLogitsE "Link to this definition")
            :   The draft logits. Expected shape: [num\_draft\_tokens, vocab\_size].

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> mAcceptanceThreshold[#](#_CPPv4N12tensorrt_llm8executor25ExternalDraftTokensConfig20mAcceptanceThresholdE "Link to this definition")
            :   The acceptance threshold. Must be > 0.f and <= 1.f.

            std::optional<bool> mFastLogits[#](#_CPPv4N12tensorrt_llm8executor25ExternalDraftTokensConfig11mFastLogitsE "Link to this definition")
            :   Use direct transfer for draft logits.

            Friends

            *friend class* Serialization

        class GuidedDecodingConfig[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfigE "Link to this definition")
        :   *#include <executor.h>*

            Guided decoding configurations for executor.

            Public Types

            enum class GuidedDecodingBackend[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig21GuidedDecodingBackendE "Link to this definition")
            :   *Values:*

                enumerator kXGRAMMAR[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig21GuidedDecodingBackend9kXGRAMMARE "Link to this definition")
                :   Enable guided decoding with XGrammar backend.

                enumerator kLLGUIDANCE[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig21GuidedDecodingBackend11kLLGUIDANCEE "Link to this definition")
                :   Enable guided decoding with LLGuidance backend.

            Public Functions

            explicit GuidedDecodingConfig( : *[GuidedDecodingBackend](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig21GuidedDecodingBackendE "tensorrt_llm::executor::GuidedDecodingConfig::GuidedDecodingBackend") backend*, : *std::optional<std::vector<std::string>> encodedVocab = std::nullopt*, : *std::optional<std::string> tokenizerStr = std::nullopt*, : *std::optional<std::vector<[TokenIdType](#_CPPv4N12tensorrt_llm8executor11TokenIdTypeE "tensorrt_llm::executor::TokenIdType")>> stopTokenIds = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig20GuidedDecodingConfigE21GuidedDecodingBackendNSt8optionalINSt6vectorINSt6stringEEEEENSt8optionalINSt6stringEEENSt8optionalINSt6vectorI11TokenIdTypeEEEE "Link to this definition")

            bool operator==(*[GuidedDecodingConfig](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfigE "tensorrt_llm::executor::GuidedDecodingConfig") const &other*) const[#](#_CPPv4NK12tensorrt_llm8executor20GuidedDecodingConfigeqERK20GuidedDecodingConfig "Link to this definition")

            void setBackend(*[GuidedDecodingBackend](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig21GuidedDecodingBackendE "tensorrt_llm::executor::GuidedDecodingConfig::GuidedDecodingBackend") const &backend*)[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig10setBackendERK21GuidedDecodingBackend "Link to this definition")

            [GuidedDecodingBackend](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig21GuidedDecodingBackendE "tensorrt_llm::executor::GuidedDecodingConfig::GuidedDecodingBackend") getBackend() const[#](#_CPPv4NK12tensorrt_llm8executor20GuidedDecodingConfig10getBackendEv "Link to this definition")

            void setEncodedVocab(*std::vector<std::string> const &encodedVocab*)[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig15setEncodedVocabERKNSt6vectorINSt6stringEEE "Link to this definition")

            std::optional<std::vector<std::string>> getEncodedVocab() const[#](#_CPPv4NK12tensorrt_llm8executor20GuidedDecodingConfig15getEncodedVocabEv "Link to this definition")

            void setTokenizerStr(*std::string const &tokenizerStr*)[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig15setTokenizerStrERKNSt6stringE "Link to this definition")

            std::optional<std::string> getTokenizerStr() const[#](#_CPPv4NK12tensorrt_llm8executor20GuidedDecodingConfig15getTokenizerStrEv "Link to this definition")

            void setStopTokenIds(*std::vector<[TokenIdType](#_CPPv4N12tensorrt_llm8executor11TokenIdTypeE "tensorrt_llm::executor::TokenIdType")> const &stopTokenIds*)[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig15setStopTokenIdsERKNSt6vectorI11TokenIdTypeEE "Link to this definition")

            std::optional<std::vector<[TokenIdType](#_CPPv4N12tensorrt_llm8executor11TokenIdTypeE "tensorrt_llm::executor::TokenIdType")>> getStopTokenIds() const[#](#_CPPv4NK12tensorrt_llm8executor20GuidedDecodingConfig15getStopTokenIdsEv "Link to this definition")

            void validate() const[#](#_CPPv4NK12tensorrt_llm8executor20GuidedDecodingConfig8validateEv "Link to this definition")

            Private Members

            [GuidedDecodingBackend](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig21GuidedDecodingBackendE "tensorrt_llm::executor::GuidedDecodingConfig::GuidedDecodingBackend") mBackend[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig8mBackendE "Link to this definition")
            :   Guided decoding backend. Currently supports XGrammar.

            std::optional<std::vector<std::string>> mEncodedVocab[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig13mEncodedVocabE "Link to this definition")
            :   Encoded vocabulary. For a huggingface tokenizer, it can be extracted by:

                ```
                encoded_vocab = tokenizer.get_vocab()
                encoded_vocab = [token for token, _ in sorted(encoded_vocab.items(), key=lambda x: x[1])]
                ```

            std::optional<std::string> mTokenizerStr[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig13mTokenizerStrE "Link to this definition")
            :   Tokenizer string. For a huggingface fast tokenizer, it can be extracted by:

                ```
                tokenizer_str = tokenizer.backend_tokenizer.to_str()
                ```

            std::optional<std::vector<[TokenIdType](#_CPPv4N12tensorrt_llm8executor11TokenIdTypeE "tensorrt_llm::executor::TokenIdType")>> mStopTokenIds[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig13mStopTokenIdsE "Link to this definition")
            :   Stop token ids. If not provided, it can be automatically detected.

            Friends

            *friend class* Serialization

        class GuidedDecodingParams[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParamsE "Link to this definition")
        :   *#include <executor.h>*

            Guided decoding parameters for a request.

            Public Types

            enum class GuideType[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams9GuideTypeE "Link to this definition")
            :   *Values:*

                enumerator kJSON[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams9GuideType5kJSONE "Link to this definition")
                :   The generated text is amenable to json format.

                enumerator kJSON\_SCHEMA[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams9GuideType12kJSON_SCHEMAE "Link to this definition")
                :   The generated text is amenable to json format with additional user-specified restrictions, namely schema.

                enumerator kREGEX[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams9GuideType6kREGEXE "Link to this definition")
                :   The generated text is amenable to the user-specified regular expression.

                enumerator kEBNF\_GRAMMAR[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams9GuideType13kEBNF_GRAMMARE "Link to this definition")
                :   The generated text is amenable to the user-specified extended Backus-Naur form (EBNF) grammar. EBNF grammar is widely-used to express context-free grammars.

                enumerator kSTRUCTURAL\_TAG[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams9GuideType15kSTRUCTURAL_TAGE "Link to this definition")
                :   The generated text is amenable to the XGrammar structural tag.

            Public Functions

            explicit GuidedDecodingParams( : *[GuideType](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams9GuideTypeE "tensorrt_llm::executor::GuidedDecodingParams::GuideType") guideType*, : *std::optional<std::string> guide = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams20GuidedDecodingParamsE9GuideTypeNSt8optionalINSt6stringEEE "Link to this definition")

            bool operator==(*[GuidedDecodingParams](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParamsE "tensorrt_llm::executor::GuidedDecodingParams") const &other*) const[#](#_CPPv4NK12tensorrt_llm8executor20GuidedDecodingParamseqERK20GuidedDecodingParams "Link to this definition")

            [GuideType](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams9GuideTypeE "tensorrt_llm::executor::GuidedDecodingParams::GuideType") getGuideType() const[#](#_CPPv4NK12tensorrt_llm8executor20GuidedDecodingParams12getGuideTypeEv "Link to this definition")

            std::optional<std::string> getGuide() const[#](#_CPPv4NK12tensorrt_llm8executor20GuidedDecodingParams8getGuideEv "Link to this definition")

            Private Members

            [GuideType](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams9GuideTypeE "tensorrt_llm::executor::GuidedDecodingParams::GuideType") mGuideType[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams10mGuideTypeE "Link to this definition")
            :   The guide type. See GuideType.

            std::optional<std::string> mGuide[#](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams6mGuideE "Link to this definition")
            :   The detailed guide string. It could be a json schema, a regular expression or a EBNF grammar depending on mGuideType.

            Friends

            *friend class* Serialization

        class JsonSerialization[#](#_CPPv4N12tensorrt_llm8executor17JsonSerializationE "Link to this definition")
        :   *#include <executor.h>*

            Class with utility functions to serialize statistics to json string.

            Public Static Functions

            static std::string toJsonStr(*[IterationStats](#_CPPv4N12tensorrt_llm8executor14IterationStatsE "tensorrt_llm::executor::IterationStats") const &iterationStats*)[#](#_CPPv4N12tensorrt_llm8executor17JsonSerialization9toJsonStrERK14IterationStats "Link to this definition")
            :   Utility function to convert an iterationStats struct to a json serialized string.

            static std::string toJsonStr( : *[RequestStatsPerIteration](#_CPPv4N12tensorrt_llm8executor24RequestStatsPerIterationE "tensorrt_llm::executor::RequestStatsPerIteration") const &requestStatsPerIter*, )[#](#_CPPv4N12tensorrt_llm8executor17JsonSerialization9toJsonStrERK24RequestStatsPerIteration "Link to this definition")
            :   Utility function to convert a requestStatsPerIteration struct to a json serialized string.

            static std::string toJsonStr(*[RequestStats](#_CPPv4N12tensorrt_llm8executor12RequestStatsE "tensorrt_llm::executor::RequestStats") const &requestStats*)[#](#_CPPv4N12tensorrt_llm8executor17JsonSerialization9toJsonStrERK12RequestStats "Link to this definition")
            :   Utility function to convert a requestStats struct to a json serialized string.

        class KvCacheConfig[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfigE "Link to this definition")
        :   *#include <executor.h>*

            Configuration class for the KV cache.

            Public Functions

            explicit KvCacheConfig( : *bool enableBlockReuse = true*, : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &maxTokens = std::nullopt*, : *std::optional<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> const &maxAttentionWindowVec = std::nullopt*, : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &sinkTokenLength = std::nullopt*, : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &freeGpuMemoryFraction = std::nullopt*, : *std::optional<size\_t> const &hostCacheSize = std::nullopt*, : *bool onboardBlocks = true*, : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &crossKvCacheFraction = std::nullopt*, : *std::optional<[RetentionPriority](#_CPPv4N12tensorrt_llm8executor17RetentionPriorityE "tensorrt_llm::executor::RetentionPriority")> secondaryOffloadMinPriority = std::nullopt*, : *size\_t eventBufferMaxSize = 0*, : *bool enablePartialReuse = true*, : *bool copyOnPartialReuse = true*, : *bool useUvm = false*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") attentionDpEventsGatherPeriodMs = 5*, : *std::optional<[tensorrt\_llm](#_CPPv412tensorrt_llm "tensorrt_llm")::[runtime](#_CPPv4N12tensorrt_llm7runtimeE "tensorrt_llm::runtime")::[RuntimeDefaults](runtime.md#_CPPv4N12tensorrt_llm7runtime15RuntimeDefaultsE "tensorrt_llm::runtime::RuntimeDefaults")> const &runtimeDefaults = std::nullopt*, : *uint64\_t const &maxGpuTotalBytes = 0*, )[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig13KvCacheConfigEbRKNSt8optionalI10SizeType32EERKNSt8optionalINSt6vectorI10SizeType32EEEERKNSt8optionalI10SizeType32EERKNSt8optionalI9FloatTypeEERKNSt8optionalI6size_tEEbRKNSt8optionalI9FloatTypeEENSt8optionalI17RetentionPriorityEE6size_tbbb10SizeType32RKNSt8optionalIN12tensorrt_llm7runtime15RuntimeDefaultsEEERK8uint64_t "Link to this definition")

            bool getEnableBlockReuse() const[#](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig19getEnableBlockReuseEv "Link to this definition")

            bool getEnablePartialReuse() const[#](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig21getEnablePartialReuseEv "Link to this definition")

            bool getCopyOnPartialReuse() const[#](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig21getCopyOnPartialReuseEv "Link to this definition")

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getMaxTokens() const[#](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig12getMaxTokensEv "Link to this definition")

            std::optional<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> getMaxAttentionWindowVec() const[#](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig24getMaxAttentionWindowVecEv "Link to this definition")

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getSinkTokenLength() const[#](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig18getSinkTokenLengthEv "Link to this definition")

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> getFreeGpuMemoryFraction() const[#](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig24getFreeGpuMemoryFractionEv "Link to this definition")

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> getCrossKvCacheFraction() const[#](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig23getCrossKvCacheFractionEv "Link to this definition")

            std::optional<size\_t> getHostCacheSize() const[#](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig16getHostCacheSizeEv "Link to this definition")

            bool getOnboardBlocks() const[#](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig16getOnboardBlocksEv "Link to this definition")

            std::optional<[RetentionPriority](#_CPPv4N12tensorrt_llm8executor17RetentionPriorityE "tensorrt_llm::executor::RetentionPriority")> getSecondaryOffloadMinPriority() const[#](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig30getSecondaryOffloadMinPriorityEv "Link to this definition")

            size\_t getEventBufferMaxSize() const[#](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig21getEventBufferMaxSizeEv "Link to this definition")

            bool getUseUvm() const[#](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig9getUseUvmEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getAttentionDpEventsGatherPeriodMs() const[#](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig34getAttentionDpEventsGatherPeriodMsEv "Link to this definition")

            uint64\_t getMaxGpuTotalBytes() const[#](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig19getMaxGpuTotalBytesEv "Link to this definition")

            void setEnableBlockReuse(*bool enableBlockReuse*)[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig19setEnableBlockReuseEb "Link to this definition")

            void setEnablePartialReuse(*bool enablePartialReuse*)[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig21setEnablePartialReuseEb "Link to this definition")

            void setCopyOnPartialReuse(*bool copyOnPartialReuse*)[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig21setCopyOnPartialReuseEb "Link to this definition")

            void setMaxTokens(*std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> maxTokens*)[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig12setMaxTokensENSt8optionalI10SizeType32EE "Link to this definition")

            void setMaxAttentionWindowVec( : *std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> maxAttentionWindowVec*, )[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig24setMaxAttentionWindowVecENSt6vectorI10SizeType32EE "Link to this definition")

            void setSinkTokenLength(*[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") sinkTokenLength*)[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig18setSinkTokenLengthE10SizeType32 "Link to this definition")

            void setFreeGpuMemoryFraction(*[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType") freeGpuMemoryFraction*)[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig24setFreeGpuMemoryFractionE9FloatType "Link to this definition")

            void setCrossKvCacheFraction(*[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType") crossKvCacheFraction*)[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig23setCrossKvCacheFractionE9FloatType "Link to this definition")

            void setHostCacheSize(*size\_t hostCacheSize*)[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig16setHostCacheSizeE6size_t "Link to this definition")

            void setOnboardBlocks(*bool onboardBlocks*)[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig16setOnboardBlocksEb "Link to this definition")

            void setSecondaryOffloadMinPriority( : *std::optional<[RetentionPriority](#_CPPv4N12tensorrt_llm8executor17RetentionPriorityE "tensorrt_llm::executor::RetentionPriority")> secondaryOffloadMinPriority*, )[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig30setSecondaryOffloadMinPriorityENSt8optionalI17RetentionPriorityEE "Link to this definition")

            void setEventBufferMaxSize(*size\_t eventBufferMaxSize*)[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig21setEventBufferMaxSizeE6size_t "Link to this definition")

            void setUseUvm(*bool useUvm*)[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig9setUseUvmEb "Link to this definition")

            void setAttentionDpEventsGatherPeriodMs( : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") attentionDpEventsGatherPeriodMs*, )[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig34setAttentionDpEventsGatherPeriodMsE10SizeType32 "Link to this definition")

            void setMaxGpuTotalBytes(*uint64\_t maxGpuTotalBytes*)[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig19setMaxGpuTotalBytesE8uint64_t "Link to this definition")

            void fillEmptyFieldsFromRuntimeDefaults( : *[tensorrt\_llm](#_CPPv412tensorrt_llm "tensorrt_llm")::[runtime](#_CPPv4N12tensorrt_llm7runtimeE "tensorrt_llm::runtime")::[RuntimeDefaults](runtime.md#_CPPv4N12tensorrt_llm7runtime15RuntimeDefaultsE "tensorrt_llm::runtime::RuntimeDefaults") const &runtimeDefaults*, )[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig34fillEmptyFieldsFromRuntimeDefaultsERKN12tensorrt_llm7runtime15RuntimeDefaultsE "Link to this definition")

            Public Static Attributes

            static constexpr auto kDefaultGpuMemFraction = 0.9F[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig22kDefaultGpuMemFractionE "Link to this definition")

            Private Members

            bool mEnableBlockReuse[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig17mEnableBlockReuseE "Link to this definition")
            :   Controls if KV cache blocks can be reused for different requests.

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> mMaxTokens[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig10mMaxTokensE "Link to this definition")
            :   The maximum number of tokens that should be stored in the KV cache If both mMaxTokens and mFreeGpuMemoryFraction are specified, memory corresponding to the minimum will be allocated.

            std::optional<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> mMaxAttentionWindowVec[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig22mMaxAttentionWindowVecE "Link to this definition")
            :   Size of the attention window for each sequence. Only the last mMaxAttentionWindow tokens of each sequence will be stored in the KV cache. Different layers may have different max attention window sizes. If the number of elements in mMaxAttentionWindowVec is less than the number of layers, mMaxAttentionWindowVec will be repeated multiple times to the number of layers.

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> mSinkTokenLength[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig16mSinkTokenLengthE "Link to this definition")
            :   Number of sink tokens (tokens to always keep in attention window)

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> mFreeGpuMemoryFraction[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig22mFreeGpuMemoryFractionE "Link to this definition")
            :   The fraction of GPU memory fraction that should be allocated for the KV cache. Default is 90%. If both mMaxTokens and mFreeGpuMemoryFraction are specified, memory corresponding to the minimum will be allocated.

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> mCrossKvCacheFraction[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig21mCrossKvCacheFractionE "Link to this definition")
            :   The fraction of the KV Cache memory should be reserved for cross attention If set to p, self attention will use 1-p of KV Cache memory and cross attention will use p of KV Cache memory. Default is 50%. Should only be set when using encoder-decoder model.

            std::optional<size\_t> mHostCacheSize[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig14mHostCacheSizeE "Link to this definition")
            :   Size of secondary memory pool in bytes. Default is 0. Having a secondary memory pool increases KV cache block reuse potential.

            bool mOnboardBlocks[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig14mOnboardBlocksE "Link to this definition")
            :   Controls whether offloaded blocks should be onboarded back into primary memory before being reused.

            std::optional<[RetentionPriority](#_CPPv4N12tensorrt_llm8executor17RetentionPriorityE "tensorrt_llm::executor::RetentionPriority")> mSecondaryOffloadMinPriority[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig28mSecondaryOffloadMinPriorityE "Link to this definition")
            :   Only blocks with priority > mSecondaryOfflineMinPriority can be offloaded to secondary memory.

            size\_t mEventBufferMaxSize[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig19mEventBufferMaxSizeE "Link to this definition")
            :   Max size of the KV cache event buffer.

            bool mEnablePartialReuse[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig19mEnablePartialReuseE "Link to this definition")
            :   Whether blocks that are only partially matched can be reused.

            bool mCopyOnPartialReuse[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig19mCopyOnPartialReuseE "Link to this definition")
            :   Whether partially matched blocks that are in use can be reused after copying them.

            bool mUseUvm[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig7mUseUvmE "Link to this definition")
            :   Whether to use UVM for the KV cache.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mAttentionDpEventsGatherPeriodMs[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig32mAttentionDpEventsGatherPeriodMsE "Link to this definition")
            :   The period in milliseconds to gather attention DP events across ranks.

            uint64\_t mMaxGpuTotalBytes[#](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig17mMaxGpuTotalBytesE "Link to this definition")
            :   The maximum size in bytes of GPU memory that can be allocated for the KV cache. If both mMaxGpuTotalBytes and mFreeGpuMemoryFraction are specified, memory corresponding to the minimum will be allocated.

            Friends

            *friend class* Serialization

        struct KVCacheCreatedData[#](#_CPPv4N12tensorrt_llm8executor18KVCacheCreatedDataE "Link to this definition")
        :   Public Members

            std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> numBlocksPerCacheLevel[#](#_CPPv4N12tensorrt_llm8executor18KVCacheCreatedData22numBlocksPerCacheLevelE "Link to this definition")
            :   The amount of blocks at each cache level.

        struct KVCacheEvent[#](#_CPPv4N12tensorrt_llm8executor12KVCacheEventE "Link to this definition")
        :   Public Functions

            KVCacheEvent( : *[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") eventId*, : *[KVCacheEventData](#_CPPv4N12tensorrt_llm8executor16KVCacheEventDataE "tensorrt_llm::executor::KVCacheEventData") data*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") windowSize*, : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> attentionDpRank = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor12KVCacheEvent12KVCacheEventE6IdType16KVCacheEventData10SizeType32NSt8optionalI10SizeType32EE "Link to this definition")

            Public Members

            [IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") eventId[#](#_CPPv4N12tensorrt_llm8executor12KVCacheEvent7eventIdE "Link to this definition")
            :   The unique id of this event.

            [KVCacheEventData](#_CPPv4N12tensorrt_llm8executor16KVCacheEventDataE "tensorrt_llm::executor::KVCacheEventData") data[#](#_CPPv4N12tensorrt_llm8executor12KVCacheEvent4dataE "Link to this definition")
            :   The data corresponding to this event.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") windowSize[#](#_CPPv4N12tensorrt_llm8executor12KVCacheEvent10windowSizeE "Link to this definition")
            :   The sliding window size.

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> attentionDpRank[#](#_CPPv4N12tensorrt_llm8executor12KVCacheEvent15attentionDpRankE "Link to this definition")
            :   The attention DP rank of the event, if applicable.

        template<typename T> struct KVCacheEventDiff[#](#_CPPv4I0EN12tensorrt_llm8executor16KVCacheEventDiffE "Link to this definition")
        :   Public Members

            [T](#_CPPv4I0EN12tensorrt_llm8executor16KVCacheEventDiffE "tensorrt_llm::executor::KVCacheEventDiff::T") oldValue[#](#_CPPv4N12tensorrt_llm8executor16KVCacheEventDiff8oldValueE "Link to this definition")

            [T](#_CPPv4I0EN12tensorrt_llm8executor16KVCacheEventDiffE "tensorrt_llm::executor::KVCacheEventDiff::T") newValue[#](#_CPPv4N12tensorrt_llm8executor16KVCacheEventDiff8newValueE "Link to this definition")

        class KVCacheEventManager[#](#_CPPv4N12tensorrt_llm8executor19KVCacheEventManagerE "Link to this definition")
        :   *#include <executor.h>*

            Exposes a limited set of KV cache manager functionalities.

            Public Functions

            KVCacheEventManager( : *std::shared\_ptr<[tensorrt\_llm](#_CPPv412tensorrt_llm "tensorrt_llm")::[batch\_manager](#_CPPv4N12tensorrt_llm13batch_managerE "tensorrt_llm::batch_manager")::[kv\_cache\_manager](#_CPPv4N12tensorrt_llm13batch_manager16kv_cache_managerE "tensorrt_llm::batch_manager::kv_cache_manager")::BaseKVCacheManager> kvCacheManager*, )[#](#_CPPv4N12tensorrt_llm8executor19KVCacheEventManager19KVCacheEventManagerENSt10shared_ptrIN12tensorrt_llm13batch_manager16kv_cache_manager18BaseKVCacheManagerEEE "Link to this definition")

            std::deque<[KVCacheEvent](#_CPPv4N12tensorrt_llm8executor12KVCacheEventE "tensorrt_llm::executor::KVCacheEvent")> getLatestEvents( : *std::optional<std::chrono::milliseconds> timeout = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor19KVCacheEventManager15getLatestEventsENSt8optionalINSt6chrono12millisecondsEEE "Link to this definition")
            :   Get the latest KV Cache events.

                Parameters:
                :   **timeout** – The maximum time to wait for new events. If nullopt, will only return when new events are available, or when the executor instance has shutdown.

            Private Members

            std::shared\_ptr<[tensorrt\_llm](#_CPPv412tensorrt_llm "tensorrt_llm")::[batch\_manager](#_CPPv4N12tensorrt_llm13batch_managerE "tensorrt_llm::batch_manager")::[kv\_cache\_manager](#_CPPv4N12tensorrt_llm13batch_manager16kv_cache_managerE "tensorrt_llm::batch_manager::kv_cache_manager")::BaseKVCacheManager> kvCacheManager[#](#_CPPv4N12tensorrt_llm8executor19KVCacheEventManager14kvCacheManagerE "Link to this definition")

        struct KVCacheRemovedData[#](#_CPPv4N12tensorrt_llm8executor18KVCacheRemovedDataE "Link to this definition")
        :   Public Members

            std::vector<[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType")> blockHashes[#](#_CPPv4N12tensorrt_llm8executor18KVCacheRemovedData11blockHashesE "Link to this definition")
            :   The hashes of blocks being removed.

        class KvCacheRetentionConfig[#](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfigE "Link to this definition")
        :   *#include <executor.h>*

            Configuration for the request’s retention in the KV Cache.

            Public Functions

            inline explicit KvCacheRetentionConfig()[#](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig22KvCacheRetentionConfigEv "Link to this definition")

            explicit KvCacheRetentionConfig( : *std::vector<[TokenRangeRetentionConfig](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfigE "tensorrt_llm::executor::KvCacheRetentionConfig::TokenRangeRetentionConfig")> const &tokenRangeRetentionPriorities*, : *[RetentionPriority](#_CPPv4N12tensorrt_llm8executor17RetentionPriorityE "tensorrt_llm::executor::RetentionPriority") decodeRetentionPriority = [kDefaultRetentionPriority](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25kDefaultRetentionPriorityE "tensorrt_llm::executor::KvCacheRetentionConfig::kDefaultRetentionPriority")*, : *std::optional<std::chrono::milliseconds> decodeDurationMs = std::nullopt*, : *[KvCacheTransferMode](#_CPPv4N12tensorrt_llm8executor19KvCacheTransferModeE "tensorrt_llm::executor::KvCacheTransferMode") transferMode = [KvCacheTransferMode](#_CPPv4N12tensorrt_llm8executor19KvCacheTransferModeE "tensorrt_llm::executor::KvCacheTransferMode")::[DRAM](#_CPPv4N12tensorrt_llm8executor19KvCacheTransferMode4DRAME "tensorrt_llm::executor::KvCacheTransferMode::DRAM")*, : *std::string const &directory = ""*, )[#](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig22KvCacheRetentionConfigERKNSt6vectorI25TokenRangeRetentionConfigEE17RetentionPriorityNSt8optionalINSt6chrono12millisecondsEEE19KvCacheTransferModeRKNSt6stringE "Link to this definition")

            std::vector<[TokenRangeRetentionConfig](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfigE "tensorrt_llm::executor::KvCacheRetentionConfig::TokenRangeRetentionConfig")> getTokenRangeRetentionConfigs() const[#](#_CPPv4NK12tensorrt_llm8executor22KvCacheRetentionConfig29getTokenRangeRetentionConfigsEv "Link to this definition")

            [RetentionPriority](#_CPPv4N12tensorrt_llm8executor17RetentionPriorityE "tensorrt_llm::executor::RetentionPriority") getDecodeRetentionPriority() const[#](#_CPPv4NK12tensorrt_llm8executor22KvCacheRetentionConfig26getDecodeRetentionPriorityEv "Link to this definition")

            std::optional<std::chrono::milliseconds> getDecodeDurationMs() const[#](#_CPPv4NK12tensorrt_llm8executor22KvCacheRetentionConfig19getDecodeDurationMsEv "Link to this definition")

            [KvCacheTransferMode](#_CPPv4N12tensorrt_llm8executor19KvCacheTransferModeE "tensorrt_llm::executor::KvCacheTransferMode") getTransferMode() const[#](#_CPPv4NK12tensorrt_llm8executor22KvCacheRetentionConfig15getTransferModeEv "Link to this definition")

            std::string const &getDirectory() const[#](#_CPPv4NK12tensorrt_llm8executor22KvCacheRetentionConfig12getDirectoryEv "Link to this definition")

            std::vector<[RetentionPriorityAndDuration](#_CPPv4N12tensorrt_llm8executor28RetentionPriorityAndDurationE "tensorrt_llm::executor::RetentionPriorityAndDuration")> getPerBlockRetentionPriorityDuration( : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") blockSize*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") seqLen*, ) const[#](#_CPPv4NK12tensorrt_llm8executor22KvCacheRetentionConfig36getPerBlockRetentionPriorityDurationE10SizeType3210SizeType32 "Link to this definition")
            :   Convert the token range data into an entry per kv block. Returns a tuple of vectors corresponding to the priorities and durations for each block.

            inline bool operator==(*[KvCacheRetentionConfig](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfigE "tensorrt_llm::executor::KvCacheRetentionConfig") const &other*) const[#](#_CPPv4NK12tensorrt_llm8executor22KvCacheRetentionConfigeqERK22KvCacheRetentionConfig "Link to this definition")

            Public Static Attributes

            static constexpr [RetentionPriority](#_CPPv4N12tensorrt_llm8executor17RetentionPriorityE "tensorrt_llm::executor::RetentionPriority") kMinRetentionPriority = 0[#](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig21kMinRetentionPriorityE "Link to this definition")

            static constexpr [RetentionPriority](#_CPPv4N12tensorrt_llm8executor17RetentionPriorityE "tensorrt_llm::executor::RetentionPriority") kMaxRetentionPriority = 100[#](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig21kMaxRetentionPriorityE "Link to this definition")

            static constexpr [RetentionPriority](#_CPPv4N12tensorrt_llm8executor17RetentionPriorityE "tensorrt_llm::executor::RetentionPriority") kDefaultRetentionPriority = 35[#](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25kDefaultRetentionPriorityE "Link to this definition")

            Private Members

            std::vector<[TokenRangeRetentionConfig](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfigE "tensorrt_llm::executor::KvCacheRetentionConfig::TokenRangeRetentionConfig")> mTokenRangeRetentionConfigs[#](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig27mTokenRangeRetentionConfigsE "Link to this definition")
            :   The token ranges and priority levels to update. Ranges must be non-overlapping. For example [(0, 64), (100, 128), (70, 80)] is valid, whereas [(0, 64), (60, 128)] is not.

            [RetentionPriority](#_CPPv4N12tensorrt_llm8executor17RetentionPriorityE "tensorrt_llm::executor::RetentionPriority") mDecodeRetentionPriority[#](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig24mDecodeRetentionPriorityE "Link to this definition")
            :   The priority level to assign to blocks allocated in the decode phase.

            std::optional<std::chrono::milliseconds> mDecodeDurationMs[#](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig17mDecodeDurationMsE "Link to this definition")
            :   The duration in ms that decode blocks should remain at their assigned priority level.

            [KvCacheTransferMode](#_CPPv4N12tensorrt_llm8executor19KvCacheTransferModeE "tensorrt_llm::executor::KvCacheTransferMode") mTransferMode[#](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig13mTransferModeE "Link to this definition")
            :   The transfer mode for the block.

            std::string mDirectory[#](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig10mDirectoryE "Link to this definition")
            :   Name of the directory if transfer mode is GDS or POSIX\_DEBUG\_FALLBACK.

            struct TokenRangeRetentionConfig[#](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfigE "Link to this definition")
            :   *#include <executor.h>*

                A single entry to set block priorities over a token range. Earlier ranges always take priority over later ones. For example, with a block size of 16, a range of [0, 17] would be applied to the first two blocks.

                Public Functions

                explicit TokenRangeRetentionConfig( : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") tokenStart*, : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> tokenEnd = std::nullopt*, : *[RetentionPriority](#_CPPv4N12tensorrt_llm8executor17RetentionPriorityE "tensorrt_llm::executor::RetentionPriority") priority = [KvCacheRetentionConfig](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfigE "tensorrt_llm::executor::KvCacheRetentionConfig")::[kDefaultRetentionPriority](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25kDefaultRetentionPriorityE "tensorrt_llm::executor::KvCacheRetentionConfig::kDefaultRetentionPriority")*, : *std::optional<std::chrono::milliseconds> durationMs = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfig25TokenRangeRetentionConfigE10SizeType32NSt8optionalI10SizeType32EE17RetentionPriorityNSt8optionalINSt6chrono12millisecondsEEE "Link to this definition")

                bool operator==(*[TokenRangeRetentionConfig](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfigE "tensorrt_llm::executor::KvCacheRetentionConfig::TokenRangeRetentionConfig") const &other*) const[#](#_CPPv4NK12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfigeqERK25TokenRangeRetentionConfig "Link to this definition")

                Public Members

                [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") tokenStart[#](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfig10tokenStartE "Link to this definition")
                :   The first token of this range.

                std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> tokenEnd[#](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfig8tokenEndE "Link to this definition")
                :   The final token of this range. The end is not included in the range. This can be set to std::nullopt to extend the range to the end of the sequence.

                [RetentionPriority](#_CPPv4N12tensorrt_llm8executor17RetentionPriorityE "tensorrt_llm::executor::RetentionPriority") priority[#](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfig8priorityE "Link to this definition")
                :   The priority of this token range. Higher priorities are less likely to be evicted or offloaded.

                std::optional<std::chrono::milliseconds> durationMs[#](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfig10durationMsE "Link to this definition")
                :   The duration in ms that the block should remain at the given priority level. Set to std::nullopt to have no expiration time, and keep the block at the given priority level until it gets reclaimed. After the duration has passed, the block will be moved back to the `kDefaultRetentionPriority` level.

        struct KVCacheStoredBlockData[#](#_CPPv4N12tensorrt_llm8executor22KVCacheStoredBlockDataE "Link to this definition")
        :   *#include <executor.h>*

            An entry for a single block stored into the tree.

            Public Functions

            inline KVCacheStoredBlockData( : *[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") blockHash*, : *[tensorrt\_llm](#_CPPv412tensorrt_llm "tensorrt_llm")::[runtime](#_CPPv4N12tensorrt_llm7runtimeE "tensorrt_llm::runtime")::[VecUniqueTokens](runtime.md#_CPPv4N12tensorrt_llm7runtime15VecUniqueTokensE "tensorrt_llm::runtime::VecUniqueTokens") tokens*, : *std::optional<[tensorrt\_llm](#_CPPv412tensorrt_llm "tensorrt_llm")::[runtime](#_CPPv4N12tensorrt_llm7runtimeE "tensorrt_llm::runtime")::[LoraTaskIdType](runtime.md#_CPPv4N12tensorrt_llm7runtime14LoraTaskIdTypeE "tensorrt_llm::runtime::LoraTaskIdType")> loraId*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") cacheLevel*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") priority*, )[#](#_CPPv4N12tensorrt_llm8executor22KVCacheStoredBlockData22KVCacheStoredBlockDataE6IdTypeN12tensorrt_llm7runtime15VecUniqueTokensENSt8optionalIN12tensorrt_llm7runtime14LoraTaskIdTypeEEE10SizeType3210SizeType32 "Link to this definition")

            Public Members

            [IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") blockHash[#](#_CPPv4N12tensorrt_llm8executor22KVCacheStoredBlockData9blockHashE "Link to this definition")
            :   The hash of the block.

            [tensorrt\_llm](#_CPPv412tensorrt_llm "tensorrt_llm")::[runtime](#_CPPv4N12tensorrt_llm7runtimeE "tensorrt_llm::runtime")::[VecUniqueTokens](runtime.md#_CPPv4N12tensorrt_llm7runtime15VecUniqueTokensE "tensorrt_llm::runtime::VecUniqueTokens") tokens[#](#_CPPv4N12tensorrt_llm8executor22KVCacheStoredBlockData6tokensE "Link to this definition")
            :   The unique tokens of the block.

            std::optional<[tensorrt\_llm](#_CPPv412tensorrt_llm "tensorrt_llm")::[runtime](#_CPPv4N12tensorrt_llm7runtimeE "tensorrt_llm::runtime")::[LoraTaskIdType](runtime.md#_CPPv4N12tensorrt_llm7runtime14LoraTaskIdTypeE "tensorrt_llm::runtime::LoraTaskIdType")> loraId[#](#_CPPv4N12tensorrt_llm8executor22KVCacheStoredBlockData6loraIdE "Link to this definition")
            :   The Lora task id of the block.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") cacheLevel[#](#_CPPv4N12tensorrt_llm8executor22KVCacheStoredBlockData10cacheLevelE "Link to this definition")
            :   The cache level of the block.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") priority[#](#_CPPv4N12tensorrt_llm8executor22KVCacheStoredBlockData8priorityE "Link to this definition")
            :   The priority of the block.

        struct KVCacheStoredData[#](#_CPPv4N12tensorrt_llm8executor17KVCacheStoredDataE "Link to this definition")
        :   Public Members

            std::optional<[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType")> parentHash[#](#_CPPv4N12tensorrt_llm8executor17KVCacheStoredData10parentHashE "Link to this definition")
            :   The parent of this sequence of stored blocks.

            std::vector<[KVCacheStoredBlockData](#_CPPv4N12tensorrt_llm8executor22KVCacheStoredBlockDataE "tensorrt_llm::executor::KVCacheStoredBlockData")> blocks[#](#_CPPv4N12tensorrt_llm8executor17KVCacheStoredData6blocksE "Link to this definition")
            :   A sequence of blocks. The parent of block `i` is block `i-1`

        struct KVCacheUpdatedData[#](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedDataE "Link to this definition")
        :   Public Functions

            inline explicit KVCacheUpdatedData(*[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") blockHash*)[#](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedData18KVCacheUpdatedDataE6IdType "Link to this definition")

            inline explicit KVCacheUpdatedData( : *[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") blockHash*, : *std::optional<[KVCacheEventDiff](#_CPPv4I0EN12tensorrt_llm8executor16KVCacheEventDiffE "tensorrt_llm::executor::KVCacheEventDiff")<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> cacheLevel*, : *std::optional<[KVCacheEventDiff](#_CPPv4I0EN12tensorrt_llm8executor16KVCacheEventDiffE "tensorrt_llm::executor::KVCacheEventDiff")<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> priority*, )[#](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedData18KVCacheUpdatedDataE6IdTypeNSt8optionalI16KVCacheEventDiffI10SizeType32EEENSt8optionalI16KVCacheEventDiffI10SizeType32EEE "Link to this definition")

            inline [KVCacheUpdatedData](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedDataE "tensorrt_llm::executor::KVCacheUpdatedData") &cacheLevelUpdated( : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") oldValue*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") newValue*, )[#](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedData17cacheLevelUpdatedE10SizeType3210SizeType32 "Link to this definition")

            inline [KVCacheUpdatedData](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedDataE "tensorrt_llm::executor::KVCacheUpdatedData") &priorityUpdated( : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") oldValue*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") newValue*, )[#](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedData15priorityUpdatedE10SizeType3210SizeType32 "Link to this definition")

            Public Members

            [IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") blockHash[#](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedData9blockHashE "Link to this definition")
            :   The hash of the updated block.

            std::optional<[KVCacheEventDiff](#_CPPv4I0EN12tensorrt_llm8executor16KVCacheEventDiffE "tensorrt_llm::executor::KVCacheEventDiff")<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> cacheLevel = std::nullopt[#](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedData10cacheLevelE "Link to this definition")
            :   The updated value of the cacheLevel field.

            std::optional<[KVCacheEventDiff](#_CPPv4I0EN12tensorrt_llm8executor16KVCacheEventDiffE "tensorrt_llm::executor::KVCacheEventDiff")<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> priority = std::nullopt[#](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedData8priorityE "Link to this definition")
            :   The updated value of the priority field.

        class LogitsPostProcessorConfig[#](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfigE "Link to this definition")
        :   Public Functions

            explicit LogitsPostProcessorConfig( : *std::optional<[LogitsPostProcessorMap](#_CPPv4N12tensorrt_llm8executor22LogitsPostProcessorMapE "tensorrt_llm::executor::LogitsPostProcessorMap")> processorMap = std::nullopt*, : *std::optional<[LogitsPostProcessorBatched](#_CPPv4N12tensorrt_llm8executor26LogitsPostProcessorBatchedE "tensorrt_llm::executor::LogitsPostProcessorBatched")> processorBatched = std::nullopt*, : *bool replicate = true*, )[#](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfig25LogitsPostProcessorConfigENSt8optionalI22LogitsPostProcessorMapEENSt8optionalI26LogitsPostProcessorBatchedEEb "Link to this definition")

            std::optional<[LogitsPostProcessorMap](#_CPPv4N12tensorrt_llm8executor22LogitsPostProcessorMapE "tensorrt_llm::executor::LogitsPostProcessorMap")> getProcessorMap() const[#](#_CPPv4NK12tensorrt_llm8executor25LogitsPostProcessorConfig15getProcessorMapEv "Link to this definition")

            std::optional<[LogitsPostProcessorBatched](#_CPPv4N12tensorrt_llm8executor26LogitsPostProcessorBatchedE "tensorrt_llm::executor::LogitsPostProcessorBatched")> getProcessorBatched() const[#](#_CPPv4NK12tensorrt_llm8executor25LogitsPostProcessorConfig19getProcessorBatchedEv "Link to this definition")

            bool getReplicate() const[#](#_CPPv4NK12tensorrt_llm8executor25LogitsPostProcessorConfig12getReplicateEv "Link to this definition")

            void setProcessorMap(*[LogitsPostProcessorMap](#_CPPv4N12tensorrt_llm8executor22LogitsPostProcessorMapE "tensorrt_llm::executor::LogitsPostProcessorMap") const &processorMap*)[#](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfig15setProcessorMapERK22LogitsPostProcessorMap "Link to this definition")

            void setProcessorBatched( : *[LogitsPostProcessorBatched](#_CPPv4N12tensorrt_llm8executor26LogitsPostProcessorBatchedE "tensorrt_llm::executor::LogitsPostProcessorBatched") const &processorBatched*, )[#](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfig19setProcessorBatchedERK26LogitsPostProcessorBatched "Link to this definition")

            void setReplicate(*bool replicate*)[#](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfig12setReplicateEb "Link to this definition")

            Private Members

            std::optional<[LogitsPostProcessorMap](#_CPPv4N12tensorrt_llm8executor22LogitsPostProcessorMapE "tensorrt_llm::executor::LogitsPostProcessorMap")> mProcessorMap[#](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfig13mProcessorMapE "Link to this definition")
            :   mapping from post processor names to non-batched post processors

            std::optional<[LogitsPostProcessorBatched](#_CPPv4N12tensorrt_llm8executor26LogitsPostProcessorBatchedE "tensorrt_llm::executor::LogitsPostProcessorBatched")> mProcessorBatched[#](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfig17mProcessorBatchedE "Link to this definition")
            :   single batched post processor

            bool mReplicate[#](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfig10mReplicateE "Link to this definition")
            :   If set to true, logits post processor will run on all TP ranks in last PP rank.

        struct LookaheadDecodingConfig[#](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfigE "Link to this definition")
        :   *#include <executor.h>*

            Configuration for Look-Ahead speculative decoding. Allows to include window size, ngram size and verification set size.

            Public Functions

            LookaheadDecodingConfig( : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") windowSize*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") ngramSize*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") verificationSetSize*, )[#](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig23LookaheadDecodingConfigE10SizeType3210SizeType3210SizeType32 "Link to this definition")

            inline explicit LookaheadDecodingConfig()[#](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig23LookaheadDecodingConfigEv "Link to this definition")

            bool operator==(*[LookaheadDecodingConfig](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfigE "tensorrt_llm::executor::LookaheadDecodingConfig") const &other*) const[#](#_CPPv4NK12tensorrt_llm8executor23LookaheadDecodingConfigeqERK23LookaheadDecodingConfig "Link to this definition")

            std::tuple<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") const, [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") const, [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") const> get() const[#](#_CPPv4NK12tensorrt_llm8executor23LookaheadDecodingConfig3getEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getWindowSize() const[#](#_CPPv4NK12tensorrt_llm8executor23LookaheadDecodingConfig13getWindowSizeEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getNgramSize() const[#](#_CPPv4NK12tensorrt_llm8executor23LookaheadDecodingConfig12getNgramSizeEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getVerificationSetSize() const[#](#_CPPv4NK12tensorrt_llm8executor23LookaheadDecodingConfig22getVerificationSetSizeEv "Link to this definition")

            std::tuple<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32"), [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32"), [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32"), [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> calculateSpeculativeResource() const[#](#_CPPv4NK12tensorrt_llm8executor23LookaheadDecodingConfig28calculateSpeculativeResourceEv "Link to this definition")
            :   return <maxDecodingTokens, maxPathLen, maxDraftTokens, maxDraftPathLen>

            bool isLE(*[LookaheadDecodingConfig](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfigE "tensorrt_llm::executor::LookaheadDecodingConfig") const &that*) const[#](#_CPPv4NK12tensorrt_llm8executor23LookaheadDecodingConfig4isLEERK23LookaheadDecodingConfig "Link to this definition")
            :   return true when `this` can be executed on resources defined by `that`

            Public Static Functions

            static std::tuple<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32"), [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32"), [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32"), [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> calculateSpeculativeResourceTuple( : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") windowSize*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") ngramSize*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") verificationSetSize*, )[#](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig33calculateSpeculativeResourceTupleE10SizeType3210SizeType3210SizeType32 "Link to this definition")

            static bool isLegal( : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") windowSize*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") ngramSize*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") verificationSetSize*, ) noexcept[#](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig7isLegalE10SizeType3210SizeType3210SizeType32 "Link to this definition")
            :   return true when the parameter combination is valid.

            Public Static Attributes

            static constexpr [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") kDefaultLookaheadDecodingWindow = 4[#](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig31kDefaultLookaheadDecodingWindowE "Link to this definition")

            static constexpr [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") kDefaultLookaheadDecodingNgram = 3[#](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig30kDefaultLookaheadDecodingNgramE "Link to this definition")

            static constexpr [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") kDefaultLookaheadDecodingVerificationSet = 4[#](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig40kDefaultLookaheadDecodingVerificationSetE "Link to this definition")

            Private Members

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mWindowSize[#](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig11mWindowSizeE "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mNgramSize[#](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig10mNgramSizeE "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mVerificationSetSize[#](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig20mVerificationSetSizeE "Link to this definition")

            Friends

            *friend class* Serialization

        class LoraConfig[#](#_CPPv4N12tensorrt_llm8executor10LoraConfigE "Link to this definition")
        :   *#include <executor.h>*

            Configuration for LoRA.

            Public Functions

            explicit LoraConfig( : *[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") taskId*, : *std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> weights = std::nullopt*, : *std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> config = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor10LoraConfig10LoraConfigE6IdTypeNSt8optionalI6TensorEENSt8optionalI6TensorEE "Link to this definition")

            [IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") getTaskId() const[#](#_CPPv4NK12tensorrt_llm8executor10LoraConfig9getTaskIdEv "Link to this definition")

            std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> getWeights() const[#](#_CPPv4NK12tensorrt_llm8executor10LoraConfig10getWeightsEv "Link to this definition")

            std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> getConfig() const[#](#_CPPv4NK12tensorrt_llm8executor10LoraConfig9getConfigEv "Link to this definition")

            Private Members

            [IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") mTaskId[#](#_CPPv4N12tensorrt_llm8executor10LoraConfig7mTaskIdE "Link to this definition")
            :   The Lora task id.

            std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> mWeights[#](#_CPPv4N12tensorrt_llm8executor10LoraConfig8mWeightsE "Link to this definition")
            :   The Lora weights. See TRT-LLM documentation for expected shapes and types.

            std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> mConfig[#](#_CPPv4N12tensorrt_llm8executor10LoraConfig7mConfigE "Link to this definition")
            :   The Lora configuration. See TRT-LLM documentation for detailed description of the config tensor.

            Friends

            *friend class* Serialization

        class MropeConfig[#](#_CPPv4N12tensorrt_llm8executor11MropeConfigE "Link to this definition")
        :   *#include <executor.h>*

            Configuration for mrope.

            Public Functions

            explicit MropeConfig( : *[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") mropeRoratySinCos*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mropePositionDeltas*, )[#](#_CPPv4N12tensorrt_llm8executor11MropeConfig11MropeConfigE6Tensor10SizeType32 "Link to this definition")

            [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") getMRopeRotaryCosSin() const[#](#_CPPv4NK12tensorrt_llm8executor11MropeConfig20getMRopeRotaryCosSinEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getMRopePositionDeltas() const[#](#_CPPv4NK12tensorrt_llm8executor11MropeConfig22getMRopePositionDeltasEv "Link to this definition")

            Private Members

            [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") mMRopeRotaryCosSin[#](#_CPPv4N12tensorrt_llm8executor11MropeConfig18mMRopeRotaryCosSinE "Link to this definition")
            :   The mrope rotary sin and cos cache. Expected shape: [maxPositionEmbeddings\*rotaryEmbeddingDim],Data type must float32.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mMRopePositionDeltas[#](#_CPPv4N12tensorrt_llm8executor11MropeConfig20mMRopePositionDeltasE "Link to this definition")
            :   The mrope position deltas.

            Friends

            *friend class* Serialization

        class MultimodalInput[#](#_CPPv4N12tensorrt_llm8executor15MultimodalInputE "Link to this definition")
        :   *#include <executor.h>*

            Multimodal input data class.

            Public Functions

            explicit MultimodalInput( : *std::vector<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> multimodalHashes*, : *std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> multimodalPositions*, : *std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> multimodalLengths*, )[#](#_CPPv4N12tensorrt_llm8executor15MultimodalInput15MultimodalInputENSt6vectorINSt6vectorI10SizeType32EEEENSt6vectorI10SizeType32EENSt6vectorI10SizeType32EE "Link to this definition")

            std::vector<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> getMultimodalHashes() const[#](#_CPPv4NK12tensorrt_llm8executor15MultimodalInput19getMultimodalHashesEv "Link to this definition")

            std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getMultimodalPositions() const[#](#_CPPv4NK12tensorrt_llm8executor15MultimodalInput22getMultimodalPositionsEv "Link to this definition")

            std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getMultimodalLengths() const[#](#_CPPv4NK12tensorrt_llm8executor15MultimodalInput20getMultimodalLengthsEv "Link to this definition")

            Private Members

            std::vector<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> mMultimodalHashes[#](#_CPPv4N12tensorrt_llm8executor15MultimodalInput17mMultimodalHashesE "Link to this definition")
            :   The multimodal hashes.

            std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> mMultimodalPositions[#](#_CPPv4N12tensorrt_llm8executor15MultimodalInput20mMultimodalPositionsE "Link to this definition")
            :   The multimodal positions.

            std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> mMultimodalLengths[#](#_CPPv4N12tensorrt_llm8executor15MultimodalInput18mMultimodalLengthsE "Link to this definition")
            :   The multimodal lengths.

            Friends

            *friend class* Serialization

        class OrchestratorConfig[#](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfigE "Link to this definition")
        :   Public Functions

            explicit OrchestratorConfig( : *bool isOrchestrator = true*, : *std::string workerExecutablePath = ""*, : *std::shared\_ptr<[mpi](#_CPPv4N12tensorrt_llm3mpiE "tensorrt_llm::mpi")::MpiComm> orchLeaderComm = nullptr*, : *bool spawnProcesses = true*, )[#](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfig18OrchestratorConfigEbNSt6stringENSt10shared_ptrIN3mpi7MpiCommEEEb "Link to this definition")

            bool getIsOrchestrator() const[#](#_CPPv4NK12tensorrt_llm8executor18OrchestratorConfig17getIsOrchestratorEv "Link to this definition")

            std::string getWorkerExecutablePath() const[#](#_CPPv4NK12tensorrt_llm8executor18OrchestratorConfig23getWorkerExecutablePathEv "Link to this definition")

            std::shared\_ptr<[mpi](#_CPPv4N12tensorrt_llm3mpiE "tensorrt_llm::mpi")::MpiComm> getOrchLeaderComm() const[#](#_CPPv4NK12tensorrt_llm8executor18OrchestratorConfig17getOrchLeaderCommEv "Link to this definition")

            bool getSpawnProcesses() const[#](#_CPPv4NK12tensorrt_llm8executor18OrchestratorConfig17getSpawnProcessesEv "Link to this definition")

            void setIsOrchestrator(*bool isOrchestrator*)[#](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfig17setIsOrchestratorEb "Link to this definition")

            void setWorkerExecutablePath(*std::string const &workerExecutablePath*)[#](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfig23setWorkerExecutablePathERKNSt6stringE "Link to this definition")

            void setOrchLeaderComm( : *std::shared\_ptr<[mpi](#_CPPv4N12tensorrt_llm3mpiE "tensorrt_llm::mpi")::MpiComm> const &orchLeaderComm*, )[#](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfig17setOrchLeaderCommERKNSt10shared_ptrIN3mpi7MpiCommEEE "Link to this definition")

            void setSpawnProcesses(*bool spawnProcesses*)[#](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfig17setSpawnProcessesEb "Link to this definition")

            Private Members

            bool mIsOrchestrator[#](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfig15mIsOrchestratorE "Link to this definition")

            std::string mWorkerExecutablePath[#](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfig21mWorkerExecutablePathE "Link to this definition")

            std::shared\_ptr<[mpi](#_CPPv4N12tensorrt_llm3mpiE "tensorrt_llm::mpi")::MpiComm> mOrchLeaderComm[#](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfig15mOrchLeaderCommE "Link to this definition")

            bool mSpawnProcesses[#](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfig15mSpawnProcessesE "Link to this definition")

        class OutputConfig[#](#_CPPv4N12tensorrt_llm8executor12OutputConfigE "Link to this definition")
        :   *#include <executor.h>*

            Configuration that controls the outputs of a [Result](#structtensorrt__llm_1_1executor_1_1Result).

            Public Functions

            explicit OutputConfig( : *bool returnLogProbs = false*, : *bool returnContextLogits = false*, : *bool returnGenerationLogits = false*, : *bool excludeInputFromOutput = false*, : *bool returnEncoderOutput = false*, : *bool returnPerfMetrics = false*, : *std::optional<std::vector<[AdditionalModelOutput](#_CPPv4N12tensorrt_llm8executor21AdditionalModelOutputE "tensorrt_llm::executor::AdditionalModelOutput")>> additionalModelOutputs = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor12OutputConfig12OutputConfigEbbbbbbNSt8optionalINSt6vectorI21AdditionalModelOutputEEEE "Link to this definition")

            Public Members

            bool returnLogProbs[#](#_CPPv4N12tensorrt_llm8executor12OutputConfig14returnLogProbsE "Link to this definition")
            :   Controls if [Result](#structtensorrt__llm_1_1executor_1_1Result) should contain log probabilities. Default is false.

            bool returnContextLogits[#](#_CPPv4N12tensorrt_llm8executor12OutputConfig19returnContextLogitsE "Link to this definition")
            :   Controls if [Result](#structtensorrt__llm_1_1executor_1_1Result) should contain the context logits. Default is false.

            bool returnGenerationLogits[#](#_CPPv4N12tensorrt_llm8executor12OutputConfig22returnGenerationLogitsE "Link to this definition")
            :   Controls if [Result](#structtensorrt__llm_1_1executor_1_1Result) should contain the generation logits. Default is false.

            bool excludeInputFromOutput[#](#_CPPv4N12tensorrt_llm8executor12OutputConfig22excludeInputFromOutputE "Link to this definition")
            :   Controls if output tokens in [Result](#structtensorrt__llm_1_1executor_1_1Result) should include the input tokens. Default is false.

            bool returnEncoderOutput[#](#_CPPv4N12tensorrt_llm8executor12OutputConfig19returnEncoderOutputE "Link to this definition")
            :   Controls if [Result](#structtensorrt__llm_1_1executor_1_1Result) should contain encoder output hidden states (for encoder-only and encoder-decoder models). Default is false.

            bool returnPerfMetrics[#](#_CPPv4N12tensorrt_llm8executor12OutputConfig17returnPerfMetricsE "Link to this definition")
            :   Controls if [Result](#structtensorrt__llm_1_1executor_1_1Result) should contain performance metrics.

            std::optional<std::vector<[AdditionalModelOutput](#_CPPv4N12tensorrt_llm8executor21AdditionalModelOutputE "tensorrt_llm::executor::AdditionalModelOutput")>> additionalModelOutputs[#](#_CPPv4N12tensorrt_llm8executor12OutputConfig22additionalModelOutputsE "Link to this definition")
            :   The additional outputs to gather from the model.

        class ParallelConfig[#](#_CPPv4N12tensorrt_llm8executor14ParallelConfigE "Link to this definition")
        :   *#include <executor.h>*

            A configuration class for the parallel execution parameters Currently only supports commType = CommunicationType::kMPI.

            Public Functions

            explicit ParallelConfig( : *[CommunicationType](#_CPPv4N12tensorrt_llm8executor17CommunicationTypeE "tensorrt_llm::executor::CommunicationType") commType = [CommunicationType](#_CPPv4N12tensorrt_llm8executor17CommunicationTypeE "tensorrt_llm::executor::CommunicationType")::[kMPI](#_CPPv4N12tensorrt_llm8executor17CommunicationType4kMPIE "tensorrt_llm::executor::CommunicationType::kMPI")*, : *[CommunicationMode](#_CPPv4N12tensorrt_llm8executor17CommunicationModeE "tensorrt_llm::executor::CommunicationMode") commMode = [CommunicationMode](#_CPPv4N12tensorrt_llm8executor17CommunicationModeE "tensorrt_llm::executor::CommunicationMode")::[kLEADER](#_CPPv4N12tensorrt_llm8executor17CommunicationMode7kLEADERE "tensorrt_llm::executor::CommunicationMode::kLEADER")*, : *std::optional<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> deviceIds = std::nullopt*, : *std::optional<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> participantIds = std::nullopt*, : *std::optional<[OrchestratorConfig](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfigE "tensorrt_llm::executor::OrchestratorConfig")> const &orchestratorConfig = std::nullopt*, : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> numNodes = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor14ParallelConfig14ParallelConfigE17CommunicationType17CommunicationModeNSt8optionalINSt6vectorI10SizeType32EEEENSt8optionalINSt6vectorI10SizeType32EEEERKNSt8optionalI18OrchestratorConfigEENSt8optionalI10SizeType32EE "Link to this definition")
            :   Constructor.

                Parameters:
                :   * **commType** – The communication type. See CommunicationType.
                    * **commMode** – The communication mode. See CommunicationMode.
                    * **deviceIds** – The IDs of the GPUs involved in the execution of the model
                    * **participantIds** – The participant IDs (MPI ranks if commType == kMPI) involved in the execution of the model. The first participant is considered to be the leader.
                    * **orchestratorConfig** – The orchestrator configuration. See [OrchestratorConfig](#classtensorrt__llm_1_1executor_1_1OrchestratorConfig).
                    * **numNodes** – The number of nodes to use for execution. Default is 1.

            [CommunicationType](#_CPPv4N12tensorrt_llm8executor17CommunicationTypeE "tensorrt_llm::executor::CommunicationType") getCommunicationType() const[#](#_CPPv4NK12tensorrt_llm8executor14ParallelConfig20getCommunicationTypeEv "Link to this definition")

            [CommunicationMode](#_CPPv4N12tensorrt_llm8executor17CommunicationModeE "tensorrt_llm::executor::CommunicationMode") getCommunicationMode() const[#](#_CPPv4NK12tensorrt_llm8executor14ParallelConfig20getCommunicationModeEv "Link to this definition")

            std::optional<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> getDeviceIds() const[#](#_CPPv4NK12tensorrt_llm8executor14ParallelConfig12getDeviceIdsEv "Link to this definition")

            std::optional<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> getParticipantIds() const[#](#_CPPv4NK12tensorrt_llm8executor14ParallelConfig17getParticipantIdsEv "Link to this definition")

            std::optional<[OrchestratorConfig](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfigE "tensorrt_llm::executor::OrchestratorConfig")> getOrchestratorConfig() const[#](#_CPPv4NK12tensorrt_llm8executor14ParallelConfig21getOrchestratorConfigEv "Link to this definition")

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getNumNodes() const[#](#_CPPv4NK12tensorrt_llm8executor14ParallelConfig11getNumNodesEv "Link to this definition")

            void setCommunicationType(*[CommunicationType](#_CPPv4N12tensorrt_llm8executor17CommunicationTypeE "tensorrt_llm::executor::CommunicationType") type*)[#](#_CPPv4N12tensorrt_llm8executor14ParallelConfig20setCommunicationTypeE17CommunicationType "Link to this definition")

            void setCommunicationMode(*[CommunicationMode](#_CPPv4N12tensorrt_llm8executor17CommunicationModeE "tensorrt_llm::executor::CommunicationMode") mode*)[#](#_CPPv4N12tensorrt_llm8executor14ParallelConfig20setCommunicationModeE17CommunicationMode "Link to this definition")

            void setDeviceIds(*std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &deviceIds*)[#](#_CPPv4N12tensorrt_llm8executor14ParallelConfig12setDeviceIdsERKNSt6vectorI10SizeType32EE "Link to this definition")

            void setParticipantIds( : *std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &participantIds*, )[#](#_CPPv4N12tensorrt_llm8executor14ParallelConfig17setParticipantIdsERKNSt6vectorI10SizeType32EE "Link to this definition")

            void setOrchestratorConfig( : *[OrchestratorConfig](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfigE "tensorrt_llm::executor::OrchestratorConfig") const &orchestratorConfig*, )[#](#_CPPv4N12tensorrt_llm8executor14ParallelConfig21setOrchestratorConfigERK18OrchestratorConfig "Link to this definition")

            void setNumNodes(*[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numNodes*)[#](#_CPPv4N12tensorrt_llm8executor14ParallelConfig11setNumNodesE10SizeType32 "Link to this definition")

            Private Members

            [CommunicationType](#_CPPv4N12tensorrt_llm8executor17CommunicationTypeE "tensorrt_llm::executor::CommunicationType") mCommType[#](#_CPPv4N12tensorrt_llm8executor14ParallelConfig9mCommTypeE "Link to this definition")
            :   The type of communication protocol used. Default is MPI.

            [CommunicationMode](#_CPPv4N12tensorrt_llm8executor17CommunicationModeE "tensorrt_llm::executor::CommunicationMode") mCommMode[#](#_CPPv4N12tensorrt_llm8executor14ParallelConfig9mCommModeE "Link to this definition")
            :   The mode of communication. See CommunicationMode.

            std::optional<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> mDeviceIds[#](#_CPPv4N12tensorrt_llm8executor14ParallelConfig10mDeviceIdsE "Link to this definition")
            :   The GPU device ids to use for executing this model.

            std::optional<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> mParticipantIds[#](#_CPPv4N12tensorrt_llm8executor14ParallelConfig15mParticipantIdsE "Link to this definition")
            :   The participant ids (MPI ranks for example) used for executing this model.

            std::optional<[OrchestratorConfig](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfigE "tensorrt_llm::executor::OrchestratorConfig")> mOrchestratorConfig[#](#_CPPv4N12tensorrt_llm8executor14ParallelConfig19mOrchestratorConfigE "Link to this definition")
            :   Optional orchestrator configuration.

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> mNumNodes[#](#_CPPv4N12tensorrt_llm8executor14ParallelConfig9mNumNodesE "Link to this definition")
            :   The number of nodes to use for execution. Default is 1.

            Friends

            *friend class* Serialization

        class PeftCacheConfig[#](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfigE "Link to this definition")
        :   *#include <executor.h>*

            config for PeftCacheManager

            Public Functions

            explicit PeftCacheConfig( : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numHostModuleLayer = 0*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numDeviceModuleLayer = 0*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") optimalAdapterSize = [kDefaultOptimalAdapterSize](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig26kDefaultOptimalAdapterSizeE "tensorrt_llm::executor::PeftCacheConfig::kDefaultOptimalAdapterSize")*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") maxAdapterSize = [kDefaultMaxAdapterSize](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig22kDefaultMaxAdapterSizeE "tensorrt_llm::executor::PeftCacheConfig::kDefaultMaxAdapterSize")*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numPutWorkers = 1*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numEnsureWorkers = 1*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numCopyStreams = 1*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") maxPagesPerBlockHost = [kDefaultMaxPagesPerBlockHost](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig28kDefaultMaxPagesPerBlockHostE "tensorrt_llm::executor::PeftCacheConfig::kDefaultMaxPagesPerBlockHost")*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") maxPagesPerBlockDevice = [kDefaultMaxPagesPerBlockDevice](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig30kDefaultMaxPagesPerBlockDeviceE "tensorrt_llm::executor::PeftCacheConfig::kDefaultMaxPagesPerBlockDevice")*, : *std::optional<float> const &deviceCachePercent = std::nullopt*, : *std::optional<size\_t> const &hostCacheSize = std::nullopt*, : *std::optional<std::string> const &loraPrefetchDir = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig15PeftCacheConfigE10SizeType3210SizeType3210SizeType3210SizeType3210SizeType3210SizeType3210SizeType3210SizeType3210SizeType32RKNSt8optionalIfEERKNSt8optionalI6size_tEERKNSt8optionalINSt6stringEEE "Link to this definition")

            bool operator==(*[PeftCacheConfig](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfigE "tensorrt_llm::executor::PeftCacheConfig") const &other*) const[#](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfigeqERK15PeftCacheConfig "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getNumHostModuleLayer() const[#](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig21getNumHostModuleLayerEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getNumDeviceModuleLayer() const[#](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig23getNumDeviceModuleLayerEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getOptimalAdapterSize() const[#](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig21getOptimalAdapterSizeEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getMaxAdapterSize() const[#](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig17getMaxAdapterSizeEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getNumPutWorkers() const[#](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig16getNumPutWorkersEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getNumEnsureWorkers() const[#](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig19getNumEnsureWorkersEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getNumCopyStreams() const[#](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig17getNumCopyStreamsEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getMaxPagesPerBlockHost() const[#](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig23getMaxPagesPerBlockHostEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getMaxPagesPerBlockDevice() const[#](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig25getMaxPagesPerBlockDeviceEv "Link to this definition")

            std::optional<float> getDeviceCachePercent() const[#](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig21getDeviceCachePercentEv "Link to this definition")

            std::optional<size\_t> getHostCacheSize() const[#](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig16getHostCacheSizeEv "Link to this definition")

            std::optional<std::string> getLoraPrefetchDir() const[#](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig18getLoraPrefetchDirEv "Link to this definition")

            Public Static Attributes

            static constexpr [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") kDefaultOptimalAdapterSize = 8[#](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig26kDefaultOptimalAdapterSizeE "Link to this definition")

            static constexpr [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") kDefaultMaxAdapterSize = 64[#](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig22kDefaultMaxAdapterSizeE "Link to this definition")

            static constexpr [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") kDefaultMaxPagesPerBlockHost = 24[#](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig28kDefaultMaxPagesPerBlockHostE "Link to this definition")

            static constexpr [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") kDefaultMaxPagesPerBlockDevice = 8[#](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig30kDefaultMaxPagesPerBlockDeviceE "Link to this definition")

            Private Members

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mNumHostModuleLayer[#](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig19mNumHostModuleLayerE "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mNumDeviceModuleLayer[#](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig21mNumDeviceModuleLayerE "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mOptimalAdapterSize[#](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig19mOptimalAdapterSizeE "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mMaxAdapterSize[#](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig15mMaxAdapterSizeE "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mNumPutWorkers[#](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig14mNumPutWorkersE "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mNumEnsureWorkers[#](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig17mNumEnsureWorkersE "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mNumCopyStreams[#](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig15mNumCopyStreamsE "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mMaxPagesPerBlockHost[#](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig21mMaxPagesPerBlockHostE "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mMaxPagesPerBlockDevice[#](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig23mMaxPagesPerBlockDeviceE "Link to this definition")

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> mDeviceCachePercent[#](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig19mDeviceCachePercentE "Link to this definition")

            std::optional<size\_t> mHostCacheSize[#](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig14mHostCacheSizeE "Link to this definition")

            std::optional<std::string> mLoraPrefetchDir[#](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig16mLoraPrefetchDirE "Link to this definition")

            Friends

            *friend class* Serialization

        class PromptTuningConfig[#](#_CPPv4N12tensorrt_llm8executor18PromptTuningConfigE "Link to this definition")
        :   *#include <executor.h>*

            Configuration for prompt tuning.

            Public Functions

            explicit PromptTuningConfig( : *[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") embeddingTable*, : *std::optional<[VecTokenExtraIds](#_CPPv4N12tensorrt_llm8executor16VecTokenExtraIdsE "tensorrt_llm::executor::VecTokenExtraIds")> inputTokenExtraIds = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor18PromptTuningConfig18PromptTuningConfigE6TensorNSt8optionalI16VecTokenExtraIdsEE "Link to this definition")

            [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") getEmbeddingTable() const[#](#_CPPv4NK12tensorrt_llm8executor18PromptTuningConfig17getEmbeddingTableEv "Link to this definition")

            std::optional<[VecTokenExtraIds](#_CPPv4N12tensorrt_llm8executor16VecTokenExtraIdsE "tensorrt_llm::executor::VecTokenExtraIds")> getInputTokenExtraIds() const[#](#_CPPv4NK12tensorrt_llm8executor18PromptTuningConfig21getInputTokenExtraIdsEv "Link to this definition")

            Private Members

            [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") mEmbeddingTable[#](#_CPPv4N12tensorrt_llm8executor18PromptTuningConfig15mEmbeddingTableE "Link to this definition")
            :   The prompt embedding table. Expected shape: [task vocab\_size, hidden\_size]. Data type must match model weights.

            std::optional<[VecTokenExtraIds](#_CPPv4N12tensorrt_llm8executor16VecTokenExtraIdsE "tensorrt_llm::executor::VecTokenExtraIds")> mInputTokenExtraIds[#](#_CPPv4N12tensorrt_llm8executor18PromptTuningConfig19mInputTokenExtraIdsE "Link to this definition")
            :   The input token extra ids for KV Cache reuse when p-tuning is enabled.

            Friends

            *friend class* Serialization

        class Request[#](#_CPPv4N12tensorrt_llm8executor7RequestE "Link to this definition")
        :   *#include <executor.h>*

            A class that holds information about the request.

            Public Functions

            Request( : *[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens") inputTokenIds*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") maxTokens*, : *bool streaming = false*, : *[SamplingConfig](#_CPPv4N12tensorrt_llm8executor14SamplingConfigE "tensorrt_llm::executor::SamplingConfig") const &samplingConfig = [SamplingConfig](#_CPPv4N12tensorrt_llm8executor14SamplingConfigE "tensorrt_llm::executor::SamplingConfig")()*, : *[OutputConfig](#_CPPv4N12tensorrt_llm8executor12OutputConfigE "tensorrt_llm::executor::OutputConfig") const &outputConfig = [OutputConfig](#_CPPv4N12tensorrt_llm8executor12OutputConfigE "tensorrt_llm::executor::OutputConfig")()*, : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &endId = std::nullopt*, : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &padId = std::nullopt*, : *std::optional<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> positionIds = std::nullopt*, : *std::optional<std::list<[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens")>> badWords = std::nullopt*, : *std::optional<std::list<[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens")>> stopWords = std::nullopt*, : *std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> embeddingBias = std::nullopt*, : *std::optional<[ExternalDraftTokensConfig](#_CPPv4N12tensorrt_llm8executor25ExternalDraftTokensConfigE "tensorrt_llm::executor::ExternalDraftTokensConfig")> externalDraftTokensConfig = std::nullopt*, : *std::optional<[PromptTuningConfig](#_CPPv4N12tensorrt_llm8executor18PromptTuningConfigE "tensorrt_llm::executor::PromptTuningConfig")> pTuningConfig = std::nullopt*, : *std::optional<[MultimodalInput](#_CPPv4N12tensorrt_llm8executor15MultimodalInputE "tensorrt_llm::executor::MultimodalInput")> multimodalInput = std::nullopt*, : *std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> multimodalEmbedding = std::nullopt*, : *std::optional<[MropeConfig](#_CPPv4N12tensorrt_llm8executor11MropeConfigE "tensorrt_llm::executor::MropeConfig")> mRopeConfig = std::nullopt*, : *std::optional<[LoraConfig](#_CPPv4N12tensorrt_llm8executor10LoraConfigE "tensorrt_llm::executor::LoraConfig")> loraConfig = std::nullopt*, : *std::optional<[LookaheadDecodingConfig](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfigE "tensorrt_llm::executor::LookaheadDecodingConfig")> lookaheadConfig = std::nullopt*, : *std::optional<[KvCacheRetentionConfig](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfigE "tensorrt_llm::executor::KvCacheRetentionConfig")> kvCacheRetentionConfig = std::nullopt*, : *std::optional<std::string> logitsPostProcessorName = std::nullopt*, : *std::optional<[LogitsPostProcessor](#_CPPv4N12tensorrt_llm8executor19LogitsPostProcessorE "tensorrt_llm::executor::LogitsPostProcessor")> logitsPostProcessor = std::nullopt*, : *std::optional<[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens")> encoderInputTokenIds = std::nullopt*, : *std::optional<[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType")> clientId = std::nullopt*, : *bool returnAllGeneratedTokens = false*, : *[PriorityType](#_CPPv4N12tensorrt_llm8executor12PriorityTypeE "tensorrt_llm::executor::PriorityType") priority = [kDefaultPriority](#_CPPv4N12tensorrt_llm8executor7Request16kDefaultPriorityE "tensorrt_llm::executor::Request::kDefaultPriority")*, : *[RequestType](#_CPPv4N12tensorrt_llm8executor11RequestTypeE "tensorrt_llm::executor::RequestType") type = [RequestType](#_CPPv4N12tensorrt_llm8executor11RequestTypeE "tensorrt_llm::executor::RequestType")::[REQUEST\_TYPE\_CONTEXT\_AND\_GENERATION](#_CPPv4N12tensorrt_llm8executor11RequestType35REQUEST_TYPE_CONTEXT_AND_GENERATIONE "tensorrt_llm::executor::RequestType::REQUEST_TYPE_CONTEXT_AND_GENERATION")*, : *std::optional<[ContextPhaseParams](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsE "tensorrt_llm::executor::ContextPhaseParams")> contextPhaseParams = std::nullopt*, : *std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> encoderInputFeatures = std::nullopt*, : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> encoderOutputLength = std::nullopt*, : *std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> crossAttentionMask = std::nullopt*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numReturnSequences = 1*, : *std::optional<[EagleConfig](#_CPPv4N12tensorrt_llm8executor11EagleConfigE "tensorrt_llm::executor::EagleConfig")> eagleConfig = std::nullopt*, : *std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> skipCrossAttnBlocks = std::nullopt*, : *std::optional<[GuidedDecodingParams](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParamsE "tensorrt_llm::executor::GuidedDecodingParams")> guidedDecodingParams = std::nullopt*, : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> languageAdapterUid = std::nullopt*, : *std::optional<[MillisecondsType](#_CPPv4N12tensorrt_llm8executor16MillisecondsTypeE "tensorrt_llm::executor::MillisecondsType")> allottedTimeMs = std::nullopt*, : *std::optional<[CacheSaltIDType](#_CPPv4N12tensorrt_llm8executor15CacheSaltIDTypeE "tensorrt_llm::executor::CacheSaltIDType")> cacheSaltID = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor7Request7RequestE9VecTokens10SizeType32bRK14SamplingConfigRK12OutputConfigRKNSt8optionalI10SizeType32EERKNSt8optionalI10SizeType32EENSt8optionalINSt6vectorI10SizeType32EEEENSt8optionalINSt4listI9VecTokensEEEENSt8optionalINSt4listI9VecTokensEEEENSt8optionalI6TensorEENSt8optionalI25ExternalDraftTokensConfigEENSt8optionalI18PromptTuningConfigEENSt8optionalI15MultimodalInputEENSt8optionalI6TensorEENSt8optionalI11MropeConfigEENSt8optionalI10LoraConfigEENSt8optionalI23LookaheadDecodingConfigEENSt8optionalI22KvCacheRetentionConfigEENSt8optionalINSt6stringEEENSt8optionalI19LogitsPostProcessorEENSt8optionalI9VecTokensEENSt8optionalI6IdTypeEEb12PriorityType11RequestTypeNSt8optionalI18ContextPhaseParamsEENSt8optionalI6TensorEENSt8optionalI10SizeType32EENSt8optionalI6TensorEE10SizeType32NSt8optionalI11EagleConfigEENSt8optionalI6TensorEENSt8optionalI20GuidedDecodingParamsEENSt8optionalI10SizeType32EENSt8optionalI16MillisecondsTypeEENSt8optionalI15CacheSaltIDTypeEE "Link to this definition")
            :   The [Request](#classtensorrt__llm_1_1executor_1_1Request) constructor.

                Parameters:
                :   * **inputTokenIds** – The input token ids
                    * **maxTokens** – The maximum number of tokens to generate
                    * **streaming** – Indicates if the responses should be streamed or not. Default is false.
                    * **samplingConfig** – The sampling configuration
                    * **outputConfig** – The output configuration
                    * **endId** – The end token id
                    * **padId** – The pad token id
                    * **positionIds** – The input position ids
                    * **badWords** – A list of bad words tokens. Each “word” can be composed of multiple tokens
                    * **stopWords** – A list of stop words tokens. Each “word” can be composed of multiple tokens
                    * **embeddingBias** – The embedding bias tensor. Expected shape is [vocab\_size]
                    * **externalDraftTokensConfig** – The speculative decoding with external draft tokens configuration
                    * **pTuningConfig** – The prompt tuning configuration
                    * **multimodalInput** – The multimodal input {multimodalHashes, multimodalPositions, multimodalLengths}
                    * **multimodalEmbedding** – The multimodal embedding tensor. Expected shape is [num\_multimodal\_tokens, hidden\_dim]
                    * **mRopeConfig** – The mrope configuration
                    * **loraConfig** – The LoRA configuration
                    * **lookaheadConfig** – The lookahead speculative decoding configuration
                    * **kvCacheRetentionConfig** – The configuration used for KV cache block eviction.
                    * **logitsPostProcessorName** – The logits postprocessor name. Must correspond to one of the logits postprocessor name provided to the [ExecutorConfig](#classtensorrt__llm_1_1executor_1_1ExecutorConfig).
                    * **logitsPostProcessor** – The logits postprocessor dynamically specified per request; only supported with replicate=false or no tensor parallelism.
                    * **encoderInputTokenIds** – The encoder input token ids for encoder-decoder models, or encoder-only models
                    * **clientId** –
                    * **returnAllGeneratedTokens** – Indicates whether to return the full beams or just the newly generated tokens after every streaming step.
                    * **priority** – Sets the execution priority of this request.
                    * **type** – Indicate the request type for disaggregated serving mode.
                    * **contextPhaseParams** – Generated token ID from context only executor.
                    * **encoderInputFeatures** – Encoder input features for multimodal models.
                    * **encoderOutputLength** – Encoder output length if encoder input and output have different lengths (due to convolution down-sampling, etc.)
                    * **crossAttentionMask** – Cross attention mask.
                    * **numReturnSequences** – The number of returning sequences.
                    * **eagleConfig** – The EAGLE speculative decoding configuration
                    * **skipCrossAttnBlocks** – Skip the cross attention transformer blocks or not.
                    * **guidedDecodingParams** – The guided decoding parameters.
                    * **languageAdapterUid** – Task Uid for language adapter.
                    * **allottedTimeMs** – The allotted time in milliseconds after which the request is cancelled with a timedOut finish reason. The request may exceed this time slightly, but at most by 1 forward pass (in pipeline parallelism that may involve multiple micro-batches). A request can be timed-out before ever being scheduled.
                    * **cacheSaltID** – Salt ID for KV cache blocks to limit the kv cache reuse to the requests with the same string.

            Request(*[Request](#_CPPv4N12tensorrt_llm8executor7Request7RequestERK7Request "tensorrt_llm::executor::Request::Request") const &other*)[#](#_CPPv4N12tensorrt_llm8executor7Request7RequestERK7Request "Link to this definition")

            Request(*[Request](#_CPPv4N12tensorrt_llm8executor7Request7RequestERR7Request "tensorrt_llm::executor::Request::Request") &&other*) noexcept[#](#_CPPv4N12tensorrt_llm8executor7Request7RequestERR7Request "Link to this definition")

            [Request](#_CPPv4N12tensorrt_llm8executor7RequestE "tensorrt_llm::executor::Request") &operator=(*[Request](#_CPPv4N12tensorrt_llm8executor7RequestE "tensorrt_llm::executor::Request") const &other*)[#](#_CPPv4N12tensorrt_llm8executor7RequestaSERK7Request "Link to this definition")

            [Request](#_CPPv4N12tensorrt_llm8executor7RequestE "tensorrt_llm::executor::Request") &operator=(*[Request](#_CPPv4N12tensorrt_llm8executor7RequestE "tensorrt_llm::executor::Request") &&other*) noexcept[#](#_CPPv4N12tensorrt_llm8executor7RequestaSERR7Request "Link to this definition")

            ~Request()[#](#_CPPv4N12tensorrt_llm8executor7RequestD0Ev "Link to this definition")

            [VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens") getInputTokenIds() const[#](#_CPPv4NK12tensorrt_llm8executor7Request16getInputTokenIdsEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getMaxTokens() const[#](#_CPPv4NK12tensorrt_llm8executor7Request12getMaxTokensEv "Link to this definition")

            bool getStreaming() const[#](#_CPPv4NK12tensorrt_llm8executor7Request12getStreamingEv "Link to this definition")

            [SamplingConfig](#_CPPv4N12tensorrt_llm8executor14SamplingConfigE "tensorrt_llm::executor::SamplingConfig") getSamplingConfig() const[#](#_CPPv4NK12tensorrt_llm8executor7Request17getSamplingConfigEv "Link to this definition")

            [OutputConfig](#_CPPv4N12tensorrt_llm8executor12OutputConfigE "tensorrt_llm::executor::OutputConfig") getOutputConfig() const[#](#_CPPv4NK12tensorrt_llm8executor7Request15getOutputConfigEv "Link to this definition")

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getEndId() const[#](#_CPPv4NK12tensorrt_llm8executor7Request8getEndIdEv "Link to this definition")

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getPadId() const[#](#_CPPv4NK12tensorrt_llm8executor7Request8getPadIdEv "Link to this definition")

            std::optional<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> getPositionIds() const[#](#_CPPv4NK12tensorrt_llm8executor7Request14getPositionIdsEv "Link to this definition")

            std::optional<std::list<[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens")>> getBadWords() const[#](#_CPPv4NK12tensorrt_llm8executor7Request11getBadWordsEv "Link to this definition")

            std::optional<std::list<[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens")>> getStopWords() const[#](#_CPPv4NK12tensorrt_llm8executor7Request12getStopWordsEv "Link to this definition")

            std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> getEmbeddingBias() const[#](#_CPPv4NK12tensorrt_llm8executor7Request16getEmbeddingBiasEv "Link to this definition")

            std::optional<[ExternalDraftTokensConfig](#_CPPv4N12tensorrt_llm8executor25ExternalDraftTokensConfigE "tensorrt_llm::executor::ExternalDraftTokensConfig")> getExternalDraftTokensConfig() const[#](#_CPPv4NK12tensorrt_llm8executor7Request28getExternalDraftTokensConfigEv "Link to this definition")

            std::optional<[PromptTuningConfig](#_CPPv4N12tensorrt_llm8executor18PromptTuningConfigE "tensorrt_llm::executor::PromptTuningConfig")> getPromptTuningConfig() const[#](#_CPPv4NK12tensorrt_llm8executor7Request21getPromptTuningConfigEv "Link to this definition")

            std::optional<[MultimodalInput](#_CPPv4N12tensorrt_llm8executor15MultimodalInputE "tensorrt_llm::executor::MultimodalInput")> getMultimodalInput() const[#](#_CPPv4NK12tensorrt_llm8executor7Request18getMultimodalInputEv "Link to this definition")

            std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> getMultimodalEmbedding() const[#](#_CPPv4NK12tensorrt_llm8executor7Request22getMultimodalEmbeddingEv "Link to this definition")

            std::optional<[MropeConfig](#_CPPv4N12tensorrt_llm8executor11MropeConfigE "tensorrt_llm::executor::MropeConfig")> getMropeConfig() const[#](#_CPPv4NK12tensorrt_llm8executor7Request14getMropeConfigEv "Link to this definition")

            std::optional<[LoraConfig](#_CPPv4N12tensorrt_llm8executor10LoraConfigE "tensorrt_llm::executor::LoraConfig")> getLoraConfig() const[#](#_CPPv4NK12tensorrt_llm8executor7Request13getLoraConfigEv "Link to this definition")

            std::optional<[LookaheadDecodingConfig](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfigE "tensorrt_llm::executor::LookaheadDecodingConfig")> getLookaheadConfig() const[#](#_CPPv4NK12tensorrt_llm8executor7Request18getLookaheadConfigEv "Link to this definition")

            std::optional<[KvCacheRetentionConfig](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfigE "tensorrt_llm::executor::KvCacheRetentionConfig")> getKvCacheRetentionConfig() const[#](#_CPPv4NK12tensorrt_llm8executor7Request25getKvCacheRetentionConfigEv "Link to this definition")

            std::optional<std::string> getLogitsPostProcessorName() const[#](#_CPPv4NK12tensorrt_llm8executor7Request26getLogitsPostProcessorNameEv "Link to this definition")

            std::optional<[LogitsPostProcessor](#_CPPv4N12tensorrt_llm8executor19LogitsPostProcessorE "tensorrt_llm::executor::LogitsPostProcessor")> getLogitsPostProcessor() const[#](#_CPPv4NK12tensorrt_llm8executor7Request22getLogitsPostProcessorEv "Link to this definition")

            std::optional<[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens")> getEncoderInputTokenIds() const[#](#_CPPv4NK12tensorrt_llm8executor7Request23getEncoderInputTokenIdsEv "Link to this definition")

            std::optional<[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType")> getClientId() const[#](#_CPPv4NK12tensorrt_llm8executor7Request11getClientIdEv "Link to this definition")

            [PriorityType](#_CPPv4N12tensorrt_llm8executor12PriorityTypeE "tensorrt_llm::executor::PriorityType") getPriority() const[#](#_CPPv4NK12tensorrt_llm8executor7Request11getPriorityEv "Link to this definition")

            bool getReturnAllGeneratedTokens() const[#](#_CPPv4NK12tensorrt_llm8executor7Request27getReturnAllGeneratedTokensEv "Link to this definition")

            std::optional<[ContextPhaseParams](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsE "tensorrt_llm::executor::ContextPhaseParams")> const &getContextPhaseParams() const[#](#_CPPv4NK12tensorrt_llm8executor7Request21getContextPhaseParamsEv "Link to this definition")

            std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> getEncoderInputFeatures() const[#](#_CPPv4NK12tensorrt_llm8executor7Request23getEncoderInputFeaturesEv "Link to this definition")

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getEncoderOutputLength() const[#](#_CPPv4NK12tensorrt_llm8executor7Request22getEncoderOutputLengthEv "Link to this definition")

            std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> getCrossAttentionMask() const[#](#_CPPv4NK12tensorrt_llm8executor7Request21getCrossAttentionMaskEv "Link to this definition")

            [RequestType](#_CPPv4N12tensorrt_llm8executor11RequestTypeE "tensorrt_llm::executor::RequestType") getRequestType() const[#](#_CPPv4NK12tensorrt_llm8executor7Request14getRequestTypeEv "Link to this definition")

            std::optional<[EagleConfig](#_CPPv4N12tensorrt_llm8executor11EagleConfigE "tensorrt_llm::executor::EagleConfig")> getEagleConfig() const[#](#_CPPv4NK12tensorrt_llm8executor7Request14getEagleConfigEv "Link to this definition")

            std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> getSkipCrossAttnBlocks() const[#](#_CPPv4NK12tensorrt_llm8executor7Request22getSkipCrossAttnBlocksEv "Link to this definition")

            std::optional<[GuidedDecodingParams](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParamsE "tensorrt_llm::executor::GuidedDecodingParams")> getGuidedDecodingParams() const[#](#_CPPv4NK12tensorrt_llm8executor7Request23getGuidedDecodingParamsEv "Link to this definition")

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getLanguageAdapterUid() const[#](#_CPPv4NK12tensorrt_llm8executor7Request21getLanguageAdapterUidEv "Link to this definition")

            std::optional<[MillisecondsType](#_CPPv4N12tensorrt_llm8executor16MillisecondsTypeE "tensorrt_llm::executor::MillisecondsType")> getAllottedTimeMs() const[#](#_CPPv4NK12tensorrt_llm8executor7Request17getAllottedTimeMsEv "Link to this definition")

            std::optional<[CacheSaltIDType](#_CPPv4N12tensorrt_llm8executor15CacheSaltIDTypeE "tensorrt_llm::executor::CacheSaltIDType")> getCacheSaltID() const[#](#_CPPv4NK12tensorrt_llm8executor7Request14getCacheSaltIDEv "Link to this definition")

            std::optional<std::vector<std::string>> getAdditionalOutputNames() const[#](#_CPPv4NK12tensorrt_llm8executor7Request24getAdditionalOutputNamesEv "Link to this definition")

            void setStreaming(*bool streaming*)[#](#_CPPv4N12tensorrt_llm8executor7Request12setStreamingEb "Link to this definition")

            void setSamplingConfig(*[SamplingConfig](#_CPPv4N12tensorrt_llm8executor14SamplingConfigE "tensorrt_llm::executor::SamplingConfig") const &config*)[#](#_CPPv4N12tensorrt_llm8executor7Request17setSamplingConfigERK14SamplingConfig "Link to this definition")

            void setOutputConfig(*[OutputConfig](#_CPPv4N12tensorrt_llm8executor12OutputConfigE "tensorrt_llm::executor::OutputConfig") const &outputConfig*)[#](#_CPPv4N12tensorrt_llm8executor7Request15setOutputConfigERK12OutputConfig "Link to this definition")

            void setEndId(*[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") endId*)[#](#_CPPv4N12tensorrt_llm8executor7Request8setEndIdE10SizeType32 "Link to this definition")

            void setPadId(*[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") padId*)[#](#_CPPv4N12tensorrt_llm8executor7Request8setPadIdE10SizeType32 "Link to this definition")

            void setPositionIds(*std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &positionIds*)[#](#_CPPv4N12tensorrt_llm8executor7Request14setPositionIdsERKNSt6vectorI10SizeType32EE "Link to this definition")

            void setBadWords(*std::list<[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens")> const &badWords*)[#](#_CPPv4N12tensorrt_llm8executor7Request11setBadWordsERKNSt4listI9VecTokensEE "Link to this definition")

            void setStopWords(*std::list<[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens")> const &stopWords*)[#](#_CPPv4N12tensorrt_llm8executor7Request12setStopWordsERKNSt4listI9VecTokensEE "Link to this definition")

            void setEmbeddingBias(*[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") const &embeddingBias*)[#](#_CPPv4N12tensorrt_llm8executor7Request16setEmbeddingBiasERK6Tensor "Link to this definition")

            void setExternalDraftTokensConfig( : *[ExternalDraftTokensConfig](#_CPPv4N12tensorrt_llm8executor25ExternalDraftTokensConfigE "tensorrt_llm::executor::ExternalDraftTokensConfig") const &externalDraftTokensConfig*, )[#](#_CPPv4N12tensorrt_llm8executor7Request28setExternalDraftTokensConfigERK25ExternalDraftTokensConfig "Link to this definition")

            void setPromptTuningConfig(*[PromptTuningConfig](#_CPPv4N12tensorrt_llm8executor18PromptTuningConfigE "tensorrt_llm::executor::PromptTuningConfig") const &pTuningConfig*)[#](#_CPPv4N12tensorrt_llm8executor7Request21setPromptTuningConfigERK18PromptTuningConfig "Link to this definition")

            void setMultimodalEmbedding(*[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") const &multimodalEmbedding*)[#](#_CPPv4N12tensorrt_llm8executor7Request22setMultimodalEmbeddingERK6Tensor "Link to this definition")

            void setMultimodalInput(*[MultimodalInput](#_CPPv4N12tensorrt_llm8executor15MultimodalInputE "tensorrt_llm::executor::MultimodalInput") const &multimodalInput*)[#](#_CPPv4N12tensorrt_llm8executor7Request18setMultimodalInputERK15MultimodalInput "Link to this definition")

            void setMropeConfig(*[MropeConfig](#_CPPv4N12tensorrt_llm8executor11MropeConfigE "tensorrt_llm::executor::MropeConfig") const &mRopeConfig*)[#](#_CPPv4N12tensorrt_llm8executor7Request14setMropeConfigERK11MropeConfig "Link to this definition")

            void setLoraConfig(*[LoraConfig](#_CPPv4N12tensorrt_llm8executor10LoraConfigE "tensorrt_llm::executor::LoraConfig") const &loraConfig*)[#](#_CPPv4N12tensorrt_llm8executor7Request13setLoraConfigERK10LoraConfig "Link to this definition")

            void setLookaheadConfig( : *[LookaheadDecodingConfig](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfigE "tensorrt_llm::executor::LookaheadDecodingConfig") const &lookaheadConfig*, )[#](#_CPPv4N12tensorrt_llm8executor7Request18setLookaheadConfigERK23LookaheadDecodingConfig "Link to this definition")

            void setKvCacheRetentionConfig( : *[KvCacheRetentionConfig](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfigE "tensorrt_llm::executor::KvCacheRetentionConfig") const &kvCacheRetentionConfig*, )[#](#_CPPv4N12tensorrt_llm8executor7Request25setKvCacheRetentionConfigERK22KvCacheRetentionConfig "Link to this definition")

            void setLogitsPostProcessorName( : *std::string const &logitsPostProcessorName*, )[#](#_CPPv4N12tensorrt_llm8executor7Request26setLogitsPostProcessorNameERKNSt6stringE "Link to this definition")

            void setLogitsPostProcessor( : *std::optional<[LogitsPostProcessor](#_CPPv4N12tensorrt_llm8executor19LogitsPostProcessorE "tensorrt_llm::executor::LogitsPostProcessor")> const &logitsPostProcessor*, )[#](#_CPPv4N12tensorrt_llm8executor7Request22setLogitsPostProcessorERKNSt8optionalI19LogitsPostProcessorEE "Link to this definition")

            void setEncoderInputTokenIds(*[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens") const &encoderInputTokenIds*)[#](#_CPPv4N12tensorrt_llm8executor7Request23setEncoderInputTokenIdsERK9VecTokens "Link to this definition")

            void setClientId(*[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") clientId*)[#](#_CPPv4N12tensorrt_llm8executor7Request11setClientIdE6IdType "Link to this definition")

            void setPriority(*[PriorityType](#_CPPv4N12tensorrt_llm8executor12PriorityTypeE "tensorrt_llm::executor::PriorityType") priority*)[#](#_CPPv4N12tensorrt_llm8executor7Request11setPriorityE12PriorityType "Link to this definition")

            void setReturnAllGeneratedTokens(*bool returnAllGeneratedTokens*)[#](#_CPPv4N12tensorrt_llm8executor7Request27setReturnAllGeneratedTokensEb "Link to this definition")

            void setRequestType(*[RequestType](#_CPPv4N12tensorrt_llm8executor11RequestTypeE "tensorrt_llm::executor::RequestType") const &requestType*)[#](#_CPPv4N12tensorrt_llm8executor7Request14setRequestTypeERK11RequestType "Link to this definition")

            void setContextPhaseParams(*[ContextPhaseParams](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsE "tensorrt_llm::executor::ContextPhaseParams") contextPhaseParams*)[#](#_CPPv4N12tensorrt_llm8executor7Request21setContextPhaseParamsE18ContextPhaseParams "Link to this definition")

            void setEncoderInputFeatures(*[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") encoderInputFeatures*)[#](#_CPPv4N12tensorrt_llm8executor7Request23setEncoderInputFeaturesE6Tensor "Link to this definition")

            void setEncoderOutputLength(*[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") encoderOutputLength*)[#](#_CPPv4N12tensorrt_llm8executor7Request22setEncoderOutputLengthE10SizeType32 "Link to this definition")

            void setCrossAttentionMask(*[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") crossAttentionMask*)[#](#_CPPv4N12tensorrt_llm8executor7Request21setCrossAttentionMaskE6Tensor "Link to this definition")

            void setEagleConfig(*std::optional<[EagleConfig](#_CPPv4N12tensorrt_llm8executor11EagleConfigE "tensorrt_llm::executor::EagleConfig")> const &eagleConfig*)[#](#_CPPv4N12tensorrt_llm8executor7Request14setEagleConfigERKNSt8optionalI11EagleConfigEE "Link to this definition")

            void setSkipCrossAttnBlocks(*[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") skipCrossAttnBlocks*)[#](#_CPPv4N12tensorrt_llm8executor7Request22setSkipCrossAttnBlocksE6Tensor "Link to this definition")

            void setGuidedDecodingParams( : *[GuidedDecodingParams](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParamsE "tensorrt_llm::executor::GuidedDecodingParams") const &guidedDecodingParams*, )[#](#_CPPv4N12tensorrt_llm8executor7Request23setGuidedDecodingParamsERK20GuidedDecodingParams "Link to this definition")

            void setLanguageAdapterUid(*[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") languageAdapterUid*)[#](#_CPPv4N12tensorrt_llm8executor7Request21setLanguageAdapterUidE10SizeType32 "Link to this definition")

            void setAllottedTimeMs(*[MillisecondsType](#_CPPv4N12tensorrt_llm8executor16MillisecondsTypeE "tensorrt_llm::executor::MillisecondsType") allottedTimeMs*)[#](#_CPPv4N12tensorrt_llm8executor7Request17setAllottedTimeMsE16MillisecondsType "Link to this definition")

            void setCacheSaltID(*[CacheSaltIDType](#_CPPv4N12tensorrt_llm8executor15CacheSaltIDTypeE "tensorrt_llm::executor::CacheSaltIDType") cacheSaltID*)[#](#_CPPv4N12tensorrt_llm8executor7Request14setCacheSaltIDE15CacheSaltIDType "Link to this definition")

            Public Static Attributes

            static constexpr [PriorityType](#_CPPv4N12tensorrt_llm8executor12PriorityTypeE "tensorrt_llm::executor::PriorityType") kDefaultPriority = 0.5[#](#_CPPv4N12tensorrt_llm8executor7Request16kDefaultPriorityE "Link to this definition")

            static auto constexpr kBatchedPostProcessorName = "batched"[#](#_CPPv4N12tensorrt_llm8executor7Request25kBatchedPostProcessorNameE "Link to this definition")
            :   This logits postprocessor name will dispatch to the batched logits postprocessor.

            static auto constexpr kDynamicPostProcessorNamePrefix = "dynamic"[#](#_CPPv4N12tensorrt_llm8executor7Request31kDynamicPostProcessorNamePrefixE "Link to this definition")
            :   Dynamic logits postprocessor name will be “dynamic” + requestId.

            Private Members

            std::unique\_ptr<Impl> mImpl[#](#_CPPv4N12tensorrt_llm8executor7Request5mImplE "Link to this definition")

            Friends

            *friend class* Serialization

        class Response[#](#_CPPv4N12tensorrt_llm8executor8ResponseE "Link to this definition")
        :   *#include <executor.h>*

            Class that holds either an error or a result.

            Public Functions

            Response( : *[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") requestId*, : *std::string errorMsg*, : *std::optional<[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType")> clientId = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor8Response8ResponseE6IdTypeNSt6stringENSt8optionalI6IdTypeEE "Link to this definition")

            Response( : *[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") requestId*, : *[Result](#_CPPv4N12tensorrt_llm8executor8Response8ResponseE6IdType6ResultNSt8optionalI6IdTypeEE "tensorrt_llm::executor::Response::Response::Result") Result*, : *std::optional<[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType")> clientId = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor8Response8ResponseE6IdType6ResultNSt8optionalI6IdTypeEE "Link to this definition")

            ~Response()[#](#_CPPv4N12tensorrt_llm8executor8ResponseD0Ev "Link to this definition")

            Response(*[Response](#_CPPv4N12tensorrt_llm8executor8Response8ResponseERK8Response "tensorrt_llm::executor::Response::Response") const &other*)[#](#_CPPv4N12tensorrt_llm8executor8Response8ResponseERK8Response "Link to this definition")

            Response(*[Response](#_CPPv4N12tensorrt_llm8executor8Response8ResponseERR8Response "tensorrt_llm::executor::Response::Response") &&other*) noexcept[#](#_CPPv4N12tensorrt_llm8executor8Response8ResponseERR8Response "Link to this definition")

            [Response](#_CPPv4N12tensorrt_llm8executor8ResponseE "tensorrt_llm::executor::Response") &operator=(*[Response](#_CPPv4N12tensorrt_llm8executor8ResponseE "tensorrt_llm::executor::Response") const &other*)[#](#_CPPv4N12tensorrt_llm8executor8ResponseaSERK8Response "Link to this definition")

            [Response](#_CPPv4N12tensorrt_llm8executor8ResponseE "tensorrt_llm::executor::Response") &operator=(*[Response](#_CPPv4N12tensorrt_llm8executor8ResponseE "tensorrt_llm::executor::Response") &&other*) noexcept[#](#_CPPv4N12tensorrt_llm8executor8ResponseaSERR8Response "Link to this definition")

            [IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") getRequestId() const[#](#_CPPv4NK12tensorrt_llm8executor8Response12getRequestIdEv "Link to this definition")
            :   Get the id of the request for which this response was generated.

            std::optional<[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType")> getClientId() const[#](#_CPPv4NK12tensorrt_llm8executor8Response11getClientIdEv "Link to this definition")
            :   Get the client id of the request for which this response was generated.

            bool hasError() const[#](#_CPPv4NK12tensorrt_llm8executor8Response8hasErrorEv "Link to this definition")
            :   Indicates if this response has an error or not.

            std::string const &getErrorMsg() const[#](#_CPPv4NK12tensorrt_llm8executor8Response11getErrorMsgEv "Link to this definition")
            :   Get the error msg for this response Will throw an exception if hasError is false.

            [Result](#_CPPv4N12tensorrt_llm8executor6ResultE "tensorrt_llm::executor::Result") const &getResult() const[#](#_CPPv4NK12tensorrt_llm8executor8Response9getResultEv "Link to this definition")
            :   Get the result for this response Will throw an exception if hasResult is true.

            Private Members

            std::unique\_ptr<Impl> mImpl[#](#_CPPv4N12tensorrt_llm8executor8Response5mImplE "Link to this definition")

            Friends

            *friend class* Serialization

        struct Result[#](#_CPPv4N12tensorrt_llm8executor6ResultE "Link to this definition")
        :   *#include <executor.h>*

            Struct that holds the generation result.

            Public Members

            bool isFinal[#](#_CPPv4N12tensorrt_llm8executor6Result7isFinalE "Link to this definition")
            :   Indicates if this is the final result for the request.

            [BeamTokens](#_CPPv4N12tensorrt_llm8executor10BeamTokensE "tensorrt_llm::executor::BeamTokens") outputTokenIds[#](#_CPPv4N12tensorrt_llm8executor6Result14outputTokenIdsE "Link to this definition")
            :   The output tokens for each beam.

            std::optional<[VecLogProbs](#_CPPv4N12tensorrt_llm8executor11VecLogProbsE "tensorrt_llm::executor::VecLogProbs")> cumLogProbs[#](#_CPPv4N12tensorrt_llm8executor6Result11cumLogProbsE "Link to this definition")
            :   The cumulative log probabilities. Size beamSize.

            std::optional<std::vector<[VecLogProbs](#_CPPv4N12tensorrt_llm8executor11VecLogProbsE "tensorrt_llm::executor::VecLogProbs")>> logProbs[#](#_CPPv4N12tensorrt_llm8executor6Result8logProbsE "Link to this definition")
            :   The log probabilities for each generated token. Size [beamSize, outputLen].

            std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> contextLogits[#](#_CPPv4N12tensorrt_llm8executor6Result13contextLogitsE "Link to this definition")
            :   The context logits. Size [promptLen, vocabSizePadded].

            std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> generationLogits[#](#_CPPv4N12tensorrt_llm8executor6Result16generationLogitsE "Link to this definition")
            :   The generation logits. Size [beamSize, maxTokens, vocabSizePadded] (non-streaming) or [maxTokens, beamSize, vocabSizePadded] (streaming and allGeneratedTokens) or [1, beamSize, vocabSizePadded] (streaming and non-allGeneratedTokens)

            std::optional<[SpeculativeDecodingFastLogitsInfo](#_CPPv4N12tensorrt_llm8executor33SpeculativeDecodingFastLogitsInfoE "tensorrt_llm::executor::SpeculativeDecodingFastLogitsInfo")> specDecFastLogitsInfo[#](#_CPPv4N12tensorrt_llm8executor6Result21specDecFastLogitsInfoE "Link to this definition")
            :   Logits information for direct transfer when using fast logits.

            std::optional<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> encoderOutput[#](#_CPPv4N12tensorrt_llm8executor6Result13encoderOutputE "Link to this definition")
            :   The encoder output. Size [encoderLen, hiddenSize].

            std::vector<[FinishReason](#_CPPv4N12tensorrt_llm8executor12FinishReasonE "tensorrt_llm::executor::FinishReason")> finishReasons[#](#_CPPv4N12tensorrt_llm8executor6Result13finishReasonsE "Link to this definition")
            :   The reason why the model stopped generating tokens for each beam in this request. Size [beamSize]. Currently only supported when beamSize is 1 and when using BatchingType::kINFLIGHT.

            std::optional<[ContextPhaseParams](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsE "tensorrt_llm::executor::ContextPhaseParams")> contextPhaseParams[#](#_CPPv4N12tensorrt_llm8executor6Result18contextPhaseParamsE "Link to this definition")
            :   The params of the context phase.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") decodingIter = {0}[#](#_CPPv4N12tensorrt_llm8executor6Result12decodingIterE "Link to this definition")
            :   The number of the decoding iterations used to generate the result. In autoregressive decoding, it is equal to the maximum length of the beam in outputTokenIds. In speculative decoding, might be less than maximum length of the beam in outputTokenIds as more than one token can be generated per iteration. Used for speculative decoding statistics.

            float avgDecodedTokensPerIter = {0.0f}[#](#_CPPv4N12tensorrt_llm8executor6Result23avgDecodedTokensPerIterE "Link to this definition")
            :   The average number of decoded tokens per iteration. For standard model it is 1. For speculative decoding model >= 1 &#8212; number of draft tokens accepted per step + 1.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") sequenceIndex = {0}[#](#_CPPv4N12tensorrt_llm8executor6Result13sequenceIndexE "Link to this definition")
            :   The index of the output sequence of this result where 0 <= sequenceIndex < numReturnSequences. In beam search (beamWidth > 1), this index will be always zero because all beams to be returned are included in this result.

            bool isSequenceFinal[#](#_CPPv4N12tensorrt_llm8executor6Result15isSequenceFinalE "Link to this definition")
            :   Indicates if this is the final result for a given sequence in the request In beam search (beamWidth > 1), the value will always equal to the value of isFinal.

            std::optional<[RequestPerfMetrics](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetricsE "tensorrt_llm::executor::RequestPerfMetrics")> requestPerfMetrics[#](#_CPPv4N12tensorrt_llm8executor6Result18requestPerfMetricsE "Link to this definition")
            :   Performance metrics if returnPerfMetrics is set in [OutputConfig](#classtensorrt__llm_1_1executor_1_1OutputConfig).

            std::vector<[AdditionalOutput](#_CPPv4N12tensorrt_llm8executor16AdditionalOutputE "tensorrt_llm::executor::AdditionalOutput")> additionalOutputs[#](#_CPPv4N12tensorrt_llm8executor6Result17additionalOutputsE "Link to this definition")
            :   The additional outputs.

        struct RetentionPriorityAndDuration[#](#_CPPv4N12tensorrt_llm8executor28RetentionPriorityAndDurationE "Link to this definition")
        :   Public Functions

            inline RetentionPriorityAndDuration( : *std::optional<[RetentionPriority](#_CPPv4N12tensorrt_llm8executor17RetentionPriorityE "tensorrt_llm::executor::RetentionPriority")> const &retentionPriority*, : *std::optional<std::chrono::milliseconds> const &durationMs*, )[#](#_CPPv4N12tensorrt_llm8executor28RetentionPriorityAndDuration28RetentionPriorityAndDurationERKNSt8optionalI17RetentionPriorityEERKNSt8optionalINSt6chrono12millisecondsEEE "Link to this definition")

            Public Members

            std::optional<[RetentionPriority](#_CPPv4N12tensorrt_llm8executor17RetentionPriorityE "tensorrt_llm::executor::RetentionPriority")> retentionPriority[#](#_CPPv4N12tensorrt_llm8executor28RetentionPriorityAndDuration17retentionPriorityE "Link to this definition")

            std::optional<std::chrono::milliseconds> durationMs[#](#_CPPv4N12tensorrt_llm8executor28RetentionPriorityAndDuration10durationMsE "Link to this definition")

        class SamplingConfig[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfigE "Link to this definition")
        :   *#include <executor.h>*

            Sampling configuration.

            Public Functions

            explicit SamplingConfig( : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") beamWidth = 1*, : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &topK = std::nullopt*, : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &topP = std::nullopt*, : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &topPMin = std::nullopt*, : *std::optional<[TokenIdType](#_CPPv4N12tensorrt_llm8executor11TokenIdTypeE "tensorrt_llm::executor::TokenIdType")> const &topPResetIds = std::nullopt*, : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &topPDecay = std::nullopt*, : *std::optional<[RandomSeedType](#_CPPv4N12tensorrt_llm8executor14RandomSeedTypeE "tensorrt_llm::executor::RandomSeedType")> const &seed = std::nullopt*, : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &temperature = std::nullopt*, : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &minTokens = std::nullopt*, : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &beamSearchDiversityRate = std::nullopt*, : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &repetitionPenalty = std::nullopt*, : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &presencePenalty = std::nullopt*, : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &frequencyPenalty = std::nullopt*, : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &lengthPenalty = std::nullopt*, : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &earlyStopping = std::nullopt*, : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &noRepeatNgramSize = std::nullopt*, : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &numReturnSequences = std::nullopt*, : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &minP = std::nullopt*, : *std::optional<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> const &beamWidthArray = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig14SamplingConfigE10SizeType32RKNSt8optionalI10SizeType32EERKNSt8optionalI9FloatTypeEERKNSt8optionalI9FloatTypeEERKNSt8optionalI11TokenIdTypeEERKNSt8optionalI9FloatTypeEERKNSt8optionalI14RandomSeedTypeEERKNSt8optionalI9FloatTypeEERKNSt8optionalI10SizeType32EERKNSt8optionalI9FloatTypeEERKNSt8optionalI9FloatTypeEERKNSt8optionalI9FloatTypeEERKNSt8optionalI9FloatTypeEERKNSt8optionalI9FloatTypeEERKNSt8optionalI10SizeType32EERKNSt8optionalI10SizeType32EERKNSt8optionalI10SizeType32EERKNSt8optionalI9FloatTypeEERKNSt8optionalINSt6vectorI10SizeType32EEEE "Link to this definition")
            :   Constructor for [SamplingConfig](#classtensorrt__llm_1_1executor_1_1SamplingConfig) See description of parameters below.

            bool operator==(*[SamplingConfig](#_CPPv4N12tensorrt_llm8executor14SamplingConfigE "tensorrt_llm::executor::SamplingConfig") const &other*) const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfigeqERK14SamplingConfig "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getBeamWidth() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig12getBeamWidthEv "Link to this definition")

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") getNumReturnBeams() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig17getNumReturnBeamsEv "Link to this definition")

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getTopK() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig7getTopKEv "Link to this definition")

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> getTopP() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig7getTopPEv "Link to this definition")

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> getTopPMin() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig10getTopPMinEv "Link to this definition")

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getTopPResetIds() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig15getTopPResetIdsEv "Link to this definition")

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> getTopPDecay() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig12getTopPDecayEv "Link to this definition")

            std::optional<[RandomSeedType](#_CPPv4N12tensorrt_llm8executor14RandomSeedTypeE "tensorrt_llm::executor::RandomSeedType")> getSeed() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig7getSeedEv "Link to this definition")

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> getTemperature() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig14getTemperatureEv "Link to this definition")

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getMinTokens() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig12getMinTokensEv "Link to this definition")

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> getBeamSearchDiversityRate() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig26getBeamSearchDiversityRateEv "Link to this definition")

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> getRepetitionPenalty() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig20getRepetitionPenaltyEv "Link to this definition")

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> getPresencePenalty() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig18getPresencePenaltyEv "Link to this definition")

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> getFrequencyPenalty() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig19getFrequencyPenaltyEv "Link to this definition")

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> getLengthPenalty() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig16getLengthPenaltyEv "Link to this definition")

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getEarlyStopping() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig16getEarlyStoppingEv "Link to this definition")

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getNoRepeatNgramSize() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig20getNoRepeatNgramSizeEv "Link to this definition")

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> getNumReturnSequences() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig21getNumReturnSequencesEv "Link to this definition")

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> getMinP() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig7getMinPEv "Link to this definition")

            std::optional<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> getBeamWidthArray() const[#](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig17getBeamWidthArrayEv "Link to this definition")

            void setBeamWidth(*[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") beamWidth*)[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig12setBeamWidthE10SizeType32 "Link to this definition")

            void setTopK(*std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &topK*)[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig7setTopKERKNSt8optionalI10SizeType32EE "Link to this definition")

            void setTopP(*std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &topP*)[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig7setTopPERKNSt8optionalI9FloatTypeEE "Link to this definition")

            void setTopPMin(*std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &topPMin*)[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig10setTopPMinERKNSt8optionalI9FloatTypeEE "Link to this definition")

            void setTopPResetIds( : *std::optional<[TokenIdType](#_CPPv4N12tensorrt_llm8executor11TokenIdTypeE "tensorrt_llm::executor::TokenIdType")> const &topPResetIds*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig15setTopPResetIdsERKNSt8optionalI11TokenIdTypeEE "Link to this definition")

            void setTopPDecay(*std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &topPDecay*)[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig12setTopPDecayERKNSt8optionalI9FloatTypeEE "Link to this definition")

            void setSeed(*std::optional<[RandomSeedType](#_CPPv4N12tensorrt_llm8executor14RandomSeedTypeE "tensorrt_llm::executor::RandomSeedType")> const &seed*)[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig7setSeedERKNSt8optionalI14RandomSeedTypeEE "Link to this definition")

            void setTemperature(*std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &temperature*)[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig14setTemperatureERKNSt8optionalI9FloatTypeEE "Link to this definition")

            void setMinTokens(*std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &minTokens*)[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig12setMinTokensERKNSt8optionalI10SizeType32EE "Link to this definition")

            void setBeamSearchDiversityRate( : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &beamSearchDiversityRate*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig26setBeamSearchDiversityRateERKNSt8optionalI9FloatTypeEE "Link to this definition")

            void setRepetitionPenalty( : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &repetitionPenalty*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig20setRepetitionPenaltyERKNSt8optionalI9FloatTypeEE "Link to this definition")

            void setPresencePenalty( : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &presencePenalty*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig18setPresencePenaltyERKNSt8optionalI9FloatTypeEE "Link to this definition")

            void setFrequencyPenalty( : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &frequencyPenalty*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig19setFrequencyPenaltyERKNSt8optionalI9FloatTypeEE "Link to this definition")

            void setLengthPenalty( : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &lengthPenalty*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig16setLengthPenaltyERKNSt8optionalI9FloatTypeEE "Link to this definition")

            void setEarlyStopping( : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &earlyStopping*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig16setEarlyStoppingERKNSt8optionalI10SizeType32EE "Link to this definition")

            void setNoRepeatNgramSize( : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &noRepeatNgramSize*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig20setNoRepeatNgramSizeERKNSt8optionalI10SizeType32EE "Link to this definition")

            void setNumReturnSequences( : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &numReturnSequences*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig21setNumReturnSequencesERKNSt8optionalI10SizeType32EE "Link to this definition")

            void setMinP(*std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &minP*)[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig7setMinPERKNSt8optionalI9FloatTypeEE "Link to this definition")

            void setBeamWidthArray( : *std::optional<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> const &beamWidthArray*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig17setBeamWidthArrayERKNSt8optionalINSt6vectorI10SizeType32EEEE "Link to this definition")

            Private Functions

            void updateNumReturnBeams()[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig20updateNumReturnBeamsEv "Link to this definition")

            Private Members

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mBeamWidth[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig10mBeamWidthE "Link to this definition")
            :   The beam width. Default is 1 which disables beam search.

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> mTopK[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig5mTopKE "Link to this definition")
            :   Controls number of logits to sample from. Default is 0 (all logits).

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> mTopP[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig5mTopPE "Link to this definition")
            :   Controls the top-P probability to sample from. Default is 0.f.

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> mTopPMin[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig8mTopPMinE "Link to this definition")
            :   Controls decay in the top-P algorithm. topPMin is lower-bound. Default is 1.e-6.

            std::optional<[TokenIdType](#_CPPv4N12tensorrt_llm8executor11TokenIdTypeE "tensorrt_llm::executor::TokenIdType")> mTopPResetIds[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig13mTopPResetIdsE "Link to this definition")
            :   Controls decay in the top-P algorithm. Indicates where to reset the decay. Default is 1.

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> mTopPDecay[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig10mTopPDecayE "Link to this definition")
            :   Controls decay in the top-P algorithm. The decay value. Default is 1.f.

            std::optional<[RandomSeedType](#_CPPv4N12tensorrt_llm8executor14RandomSeedTypeE "tensorrt_llm::executor::RandomSeedType")> mSeed[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig5mSeedE "Link to this definition")
            :   Controls the random seed used by the random number generator in sampling. Default is 0.

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> mTemperature[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig12mTemperatureE "Link to this definition")
            :   Controls the modulation of logits when sampling new tokens. It can have values > 0.f. Default is 1.0f.

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> mMinTokens[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig10mMinTokensE "Link to this definition")
            :   Lower bound on the number of tokens to generate. Values < 1 have no effect. Default is 1.

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> mBeamSearchDiversityRate[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig24mBeamSearchDiversityRateE "Link to this definition")
            :   Controls the diversity in beam search.

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> mRepetitionPenalty[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig18mRepetitionPenaltyE "Link to this definition")
            :   Used to penalize tokens based on how often they appear in the sequence. It can have any value > 0.f. Values < 1.f encourages repetition, values > 1.f discourages it. Default is 1.f.

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> mPresencePenalty[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig16mPresencePenaltyE "Link to this definition")
            :   Used to penalize tokens already present in the sequence (irrespective of the number of appearances). It can have any values. Values < 0.f encourage repetition, values > 0.f discourage it. Default is 0.f.

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> mFrequencyPenalty[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig17mFrequencyPenaltyE "Link to this definition")
            :   Used to penalize tokens already present in the sequence (dependent on the number of appearances). It can have any values. Values < 0.f encourage repetition, values > 0.f discourage it. Default is 0.f.

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> mLengthPenalty[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig14mLengthPenaltyE "Link to this definition")
            :   Controls how to penalize longer sequences in beam search. Default is 0.f.

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> mEarlyStopping[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig14mEarlyStoppingE "Link to this definition")
            :   Controls whether the generation process finishes once beamWidth sentences are generated (ends with end\_token). Default is 1.

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> mNoRepeatNgramSize[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig18mNoRepeatNgramSizeE "Link to this definition")
            :   Controls how many repeat ngram size are acceptable. Default is 1 << 30.

            std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> mNumReturnSequences[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig19mNumReturnSequencesE "Link to this definition")
            :   The number of return sequences or beams. In beam search, the value should be less than or equal to mBeamWidth. In sampling, it specifies the total number of independently generated sequences.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") mNumReturnBeams[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig15mNumReturnBeamsE "Link to this definition")
            :   The number of beams to return. It is equal to beamWidth unless numReturnSequences is set. If beamWidth > 1 and numReturnSequences is set, then numReturnBeams is equal to numReturnSequences.

            std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> mMinP[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig5mMinPE "Link to this definition")
            :   Controls the min\_p scaling for sampling. It masks x which P\_x < min\_p \* P\_max, where P\_x is probability of candidate x. Default is 0.f.

            std::optional<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> mBeamWidthArray[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig15mBeamWidthArrayE "Link to this definition")
            :   Controls the beam width for each step for Variable-Beam-Width-Search.

            Private Static Functions

            static [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") checkBeamWidth(*[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") beamWidth*)[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig14checkBeamWidthE10SizeType32 "Link to this definition")

            static std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &checkTopK( : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &topK*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig9checkTopKERKNSt8optionalI9FloatTypeEE "Link to this definition")

            static std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &checkTopP( : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &topP*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig9checkTopPERKNSt8optionalI9FloatTypeEE "Link to this definition")

            static std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &checkTopPMin( : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &topPMin*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig12checkTopPMinERKNSt8optionalI9FloatTypeEE "Link to this definition")

            static std::optional<[TokenIdType](#_CPPv4N12tensorrt_llm8executor11TokenIdTypeE "tensorrt_llm::executor::TokenIdType")> const &checkTopPResetIds( : *std::optional<[TokenIdType](#_CPPv4N12tensorrt_llm8executor11TokenIdTypeE "tensorrt_llm::executor::TokenIdType")> const &topPResetIds*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig17checkTopPResetIdsERKNSt8optionalI11TokenIdTypeEE "Link to this definition")

            static std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &checkTopPDecay( : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &topPDecay*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig14checkTopPDecayERKNSt8optionalI9FloatTypeEE "Link to this definition")

            static std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &checkTemperature( : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &temperature*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig16checkTemperatureERKNSt8optionalI9FloatTypeEE "Link to this definition")

            static std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &checkMinTokens( : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &minTokens*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig14checkMinTokensERKNSt8optionalI10SizeType32EE "Link to this definition")

            static std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &checkBeamSearchDiversityRate( : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &beamSearchDiversityRate*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig28checkBeamSearchDiversityRateERKNSt8optionalI9FloatTypeEE "Link to this definition")

            static std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &checkRepetitionPenalty( : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &repetitionpenalty*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig22checkRepetitionPenaltyERKNSt8optionalI9FloatTypeEE "Link to this definition")

            static std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &checkLengthPenalty( : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &lengthPenalty*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig18checkLengthPenaltyERKNSt8optionalI9FloatTypeEE "Link to this definition")

            static std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &checkEarlyStopping( : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &earlyStopping*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig18checkEarlyStoppingERKNSt8optionalI10SizeType32EE "Link to this definition")

            static std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &checkNoRepeatNgramSize( : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &noRepeatNgramSize*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig22checkNoRepeatNgramSizeERKNSt8optionalI10SizeType32EE "Link to this definition")

            static std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &checkNumReturnSequences( : *std::optional<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")> const &numReturnSequences*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") beamWidth*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig23checkNumReturnSequencesERKNSt8optionalI10SizeType32EE10SizeType32 "Link to this definition")

            static std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &checkMinP( : *std::optional<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")> const &minP*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig9checkMinPERKNSt8optionalI9FloatTypeEE "Link to this definition")

            static std::pair<std::optional<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> const&, [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") const> const checkBeamWidthArray( : *std::optional<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>> const &beamWidthArray*, : *[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") const beamWidth*, )[#](#_CPPv4N12tensorrt_llm8executor14SamplingConfig19checkBeamWidthArrayERKNSt8optionalINSt6vectorI10SizeType32EEEEK10SizeType32 "Link to this definition")

            Friends

            *friend class* Serialization

        class SchedulerConfig[#](#_CPPv4N12tensorrt_llm8executor15SchedulerConfigE "Link to this definition")
        :   *#include <executor.h>*

            Configuration class for the scheduler.

            Public Functions

            explicit SchedulerConfig( : *[CapacitySchedulerPolicy](#_CPPv4N12tensorrt_llm8executor23CapacitySchedulerPolicyE "tensorrt_llm::executor::CapacitySchedulerPolicy") capacitySchedulerPolicy = [CapacitySchedulerPolicy](#_CPPv4N12tensorrt_llm8executor23CapacitySchedulerPolicyE "tensorrt_llm::executor::CapacitySchedulerPolicy")::[kGUARANTEED\_NO\_EVICT](#_CPPv4N12tensorrt_llm8executor23CapacitySchedulerPolicy20kGUARANTEED_NO_EVICTE "tensorrt_llm::executor::CapacitySchedulerPolicy::kGUARANTEED_NO_EVICT")*, : *std::optional<[ContextChunkingPolicy](#_CPPv4N12tensorrt_llm8executor21ContextChunkingPolicyE "tensorrt_llm::executor::ContextChunkingPolicy")> contextChunkingPolicy = std::nullopt*, : *std::optional<[DynamicBatchConfig](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfigE "tensorrt_llm::executor::DynamicBatchConfig")> dynamicBatchConfig = std::nullopt*, )[#](#_CPPv4N12tensorrt_llm8executor15SchedulerConfig15SchedulerConfigE23CapacitySchedulerPolicyNSt8optionalI21ContextChunkingPolicyEENSt8optionalI18DynamicBatchConfigEE "Link to this definition")

            bool operator==(*[SchedulerConfig](#_CPPv4N12tensorrt_llm8executor15SchedulerConfigE "tensorrt_llm::executor::SchedulerConfig") const &other*) const[#](#_CPPv4NK12tensorrt_llm8executor15SchedulerConfigeqERK15SchedulerConfig "Link to this definition")

            [CapacitySchedulerPolicy](#_CPPv4N12tensorrt_llm8executor23CapacitySchedulerPolicyE "tensorrt_llm::executor::CapacitySchedulerPolicy") getCapacitySchedulerPolicy() const[#](#_CPPv4NK12tensorrt_llm8executor15SchedulerConfig26getCapacitySchedulerPolicyEv "Link to this definition")

            std::optional<[ContextChunkingPolicy](#_CPPv4N12tensorrt_llm8executor21ContextChunkingPolicyE "tensorrt_llm::executor::ContextChunkingPolicy")> getContextChunkingPolicy() const[#](#_CPPv4NK12tensorrt_llm8executor15SchedulerConfig24getContextChunkingPolicyEv "Link to this definition")

            std::optional<[DynamicBatchConfig](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfigE "tensorrt_llm::executor::DynamicBatchConfig")> getDynamicBatchConfig() const[#](#_CPPv4NK12tensorrt_llm8executor15SchedulerConfig21getDynamicBatchConfigEv "Link to this definition")

            Private Members

            [CapacitySchedulerPolicy](#_CPPv4N12tensorrt_llm8executor23CapacitySchedulerPolicyE "tensorrt_llm::executor::CapacitySchedulerPolicy") mCapacitySchedulerPolicy[#](#_CPPv4N12tensorrt_llm8executor15SchedulerConfig24mCapacitySchedulerPolicyE "Link to this definition")
            :   The capacity scheduler policy. See CapacitySchedulerPolicy.

            std::optional<[ContextChunkingPolicy](#_CPPv4N12tensorrt_llm8executor21ContextChunkingPolicyE "tensorrt_llm::executor::ContextChunkingPolicy")> mContextChunkingPolicy[#](#_CPPv4N12tensorrt_llm8executor15SchedulerConfig22mContextChunkingPolicyE "Link to this definition")
            :   The context chunking policy. See ContextChunkingPolicy.

            std::optional<[DynamicBatchConfig](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfigE "tensorrt_llm::executor::DynamicBatchConfig")> mDynamicBatchConfig[#](#_CPPv4N12tensorrt_llm8executor15SchedulerConfig19mDynamicBatchConfigE "Link to this definition")
            :   The config for tuning batch size dynamically. See DynamicBatchSizeConfig.

            Friends

            *friend class* Serialization

        class SpeculativeDecodingConfig[#](#_CPPv4N12tensorrt_llm8executor25SpeculativeDecodingConfigE "Link to this definition")
        :   *#include <executor.h>*

            Configuration for speculative decoding (both draft and target models)

            Public Functions

            explicit SpeculativeDecodingConfig(*bool fastLogits = false*)[#](#_CPPv4N12tensorrt_llm8executor25SpeculativeDecodingConfig25SpeculativeDecodingConfigEb "Link to this definition")

            bool operator==(*[SpeculativeDecodingConfig](#_CPPv4N12tensorrt_llm8executor25SpeculativeDecodingConfigE "tensorrt_llm::executor::SpeculativeDecodingConfig") const &other*) const[#](#_CPPv4NK12tensorrt_llm8executor25SpeculativeDecodingConfigeqERK25SpeculativeDecodingConfig "Link to this definition")

            Public Members

            bool fastLogits[#](#_CPPv4N12tensorrt_llm8executor25SpeculativeDecodingConfig10fastLogitsE "Link to this definition")
            :   Send logits tensor directly from draft to target model.

            Friends

            *friend class* Serialization

        struct SpeculativeDecodingFastLogitsInfo[#](#_CPPv4N12tensorrt_llm8executor33SpeculativeDecodingFastLogitsInfoE "Link to this definition")
        :   *#include <executor.h>*

            Struct that holds the logits information when using direct transfer.

            Public Functions

            [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor") toTensor() const[#](#_CPPv4NK12tensorrt_llm8executor33SpeculativeDecodingFastLogitsInfo8toTensorEv "Link to this definition")
            :   Returns the struct serialized into a tensor that can be used as generation logits input.

            Public Members

            uint64\_t draftRequestId[#](#_CPPv4N12tensorrt_llm8executor33SpeculativeDecodingFastLogitsInfo14draftRequestIdE "Link to this definition")
            :   Draft request id.

            int32\_t draftParticipantId[#](#_CPPv4N12tensorrt_llm8executor33SpeculativeDecodingFastLogitsInfo18draftParticipantIdE "Link to this definition")
            :   MPI world rank of the draft model leader.

    namespace mpi[#](#_CPPv4N12tensorrt_llm3mpiE "Link to this definition")

## types.h[#](#types-h "Link to this heading")

namespace tensorrt\_llm
:   namespace executor
    :   Typedefs

        using TensorPtr = std::shared\_ptr<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")>[#](#_CPPv4N12tensorrt_llm8executor9TensorPtrE "Link to this definition")

        using SizeType32 = std::int32\_t[#](#_CPPv4N12tensorrt_llm8executor10SizeType32E "Link to this definition")

        using SizeType64 = std::int64\_t[#](#_CPPv4N12tensorrt_llm8executor10SizeType64E "Link to this definition")

        using FloatType = float[#](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "Link to this definition")

        using TokenIdType = std::int32\_t[#](#_CPPv4N12tensorrt_llm8executor11TokenIdTypeE "Link to this definition")

        using VecTokens = std::vector<[TokenIdType](#_CPPv4N12tensorrt_llm8executor11TokenIdTypeE "tensorrt_llm::executor::TokenIdType")>[#](#_CPPv4N12tensorrt_llm8executor9VecTokensE "Link to this definition")

        using BeamTokens = std::vector<[VecTokens](#_CPPv4N12tensorrt_llm8executor9VecTokensE "tensorrt_llm::executor::VecTokens")>[#](#_CPPv4N12tensorrt_llm8executor10BeamTokensE "Link to this definition")

        using IdType = std::uint64\_t[#](#_CPPv4N12tensorrt_llm8executor6IdTypeE "Link to this definition")

        using VecTokenExtraIds = std::vector<[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType")>[#](#_CPPv4N12tensorrt_llm8executor16VecTokenExtraIdsE "Link to this definition")

        using IterationType = std::uint64\_t[#](#_CPPv4N12tensorrt_llm8executor13IterationTypeE "Link to this definition")

        using RandomSeedType = std::uint64\_t[#](#_CPPv4N12tensorrt_llm8executor14RandomSeedTypeE "Link to this definition")

        using VecLogProbs = std::vector<[FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType")>[#](#_CPPv4N12tensorrt_llm8executor11VecLogProbsE "Link to this definition")

        using StreamPtr = std::shared\_ptr<[tensorrt\_llm](#_CPPv412tensorrt_llm "tensorrt_llm")::[runtime](#_CPPv4N12tensorrt_llm7runtimeE "tensorrt_llm::runtime")::[CudaStream](runtime.md#_CPPv4N12tensorrt_llm7runtime10CudaStreamE "tensorrt_llm::runtime::CudaStream")>[#](#_CPPv4N12tensorrt_llm8executor9StreamPtrE "Link to this definition")

        using MillisecondsType = std::chrono::milliseconds[#](#_CPPv4N12tensorrt_llm8executor16MillisecondsTypeE "Link to this definition")

        using CacheSaltIDType = std::uint64\_t[#](#_CPPv4N12tensorrt_llm8executor15CacheSaltIDTypeE "Link to this definition")

        using LogitsPostProcessor = std::function<void([IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType"), [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")&, [BeamTokens](#_CPPv4N12tensorrt_llm8executor10BeamTokensE "tensorrt_llm::executor::BeamTokens") const&, [StreamPtr](#_CPPv4N12tensorrt_llm8executor9StreamPtrE "tensorrt_llm::executor::StreamPtr") const&, std::optional<[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType")>)>[#](#_CPPv4N12tensorrt_llm8executor19LogitsPostProcessorE "Link to this definition")

        using LogitsPostProcessorMap = std::unordered\_map<std::string, [LogitsPostProcessor](#_CPPv4N12tensorrt_llm8executor19LogitsPostProcessorE "tensorrt_llm::executor::LogitsPostProcessor")>[#](#_CPPv4N12tensorrt_llm8executor22LogitsPostProcessorMapE "Link to this definition")

        using LogitsPostProcessorBatched = std::function<void(std::vector<[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType")> const&, std::vector<[Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")>&, std::vector<std::reference\_wrapper<[BeamTokens](#_CPPv4N12tensorrt_llm8executor10BeamTokensE "tensorrt_llm::executor::BeamTokens") const>> const&, [StreamPtr](#_CPPv4N12tensorrt_llm8executor9StreamPtrE "tensorrt_llm::executor::StreamPtr") const&, std::vector<std::optional<[IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType")>> const&)>[#](#_CPPv4N12tensorrt_llm8executor26LogitsPostProcessorBatchedE "Link to this definition")

        using MedusaChoices = std::vector<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>>[#](#_CPPv4N12tensorrt_llm8executor13MedusaChoicesE "Link to this definition")

        using EagleChoices = std::vector<std::vector<[SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32")>>[#](#_CPPv4N12tensorrt_llm8executor12EagleChoicesE "Link to this definition")

        using PriorityType = float[#](#_CPPv4N12tensorrt_llm8executor12PriorityTypeE "Link to this definition")

        using BufferView = std::basic\_string\_view<uint8\_t>[#](#_CPPv4N12tensorrt_llm8executor10BufferViewE "Link to this definition")

        Enums

        enum class DataType[#](#_CPPv4N12tensorrt_llm8executor8DataTypeE "Link to this definition")
        :   *Values:*

            enumerator kBOOL[#](#_CPPv4N12tensorrt_llm8executor8DataType5kBOOLE "Link to this definition")

            enumerator kUINT8[#](#_CPPv4N12tensorrt_llm8executor8DataType6kUINT8E "Link to this definition")

            enumerator kINT8[#](#_CPPv4N12tensorrt_llm8executor8DataType5kINT8E "Link to this definition")

            enumerator kINT32[#](#_CPPv4N12tensorrt_llm8executor8DataType6kINT32E "Link to this definition")

            enumerator kINT64[#](#_CPPv4N12tensorrt_llm8executor8DataType6kINT64E "Link to this definition")

            enumerator kBF16[#](#_CPPv4N12tensorrt_llm8executor8DataType5kBF16E "Link to this definition")

            enumerator kFP8[#](#_CPPv4N12tensorrt_llm8executor8DataType4kFP8E "Link to this definition")

            enumerator kFP16[#](#_CPPv4N12tensorrt_llm8executor8DataType5kFP16E "Link to this definition")

            enumerator kFP32[#](#_CPPv4N12tensorrt_llm8executor8DataType5kFP32E "Link to this definition")

            enumerator kUNKNOWN[#](#_CPPv4N12tensorrt_llm8executor8DataType8kUNKNOWNE "Link to this definition")

        enum class RequestType[#](#_CPPv4N12tensorrt_llm8executor11RequestTypeE "Link to this definition")
        :   *Values:*

            enumerator REQUEST\_TYPE\_CONTEXT\_AND\_GENERATION[#](#_CPPv4N12tensorrt_llm8executor11RequestType35REQUEST_TYPE_CONTEXT_AND_GENERATIONE "Link to this definition")

            enumerator REQUEST\_TYPE\_CONTEXT\_ONLY[#](#_CPPv4N12tensorrt_llm8executor11RequestType25REQUEST_TYPE_CONTEXT_ONLYE "Link to this definition")

            enumerator REQUEST\_TYPE\_GENERATION\_ONLY[#](#_CPPv4N12tensorrt_llm8executor11RequestType28REQUEST_TYPE_GENERATION_ONLYE "Link to this definition")

        enum class MemoryType[#](#_CPPv4N12tensorrt_llm8executor10MemoryTypeE "Link to this definition")
        :   *Values:*

            enumerator kCPU[#](#_CPPv4N12tensorrt_llm8executor10MemoryType4kCPUE "Link to this definition")

            enumerator kCPU\_PINNED[#](#_CPPv4N12tensorrt_llm8executor10MemoryType11kCPU_PINNEDE "Link to this definition")

            enumerator kCPU\_PINNEDPOOL[#](#_CPPv4N12tensorrt_llm8executor10MemoryType15kCPU_PINNEDPOOLE "Link to this definition")

            enumerator kGPU[#](#_CPPv4N12tensorrt_llm8executor10MemoryType4kGPUE "Link to this definition")

            enumerator kUVM[#](#_CPPv4N12tensorrt_llm8executor10MemoryType4kUVME "Link to this definition")

            enumerator kUNKNOWN[#](#_CPPv4N12tensorrt_llm8executor10MemoryType8kUNKNOWNE "Link to this definition")

        enum class ModelType[#](#_CPPv4N12tensorrt_llm8executor9ModelTypeE "Link to this definition")
        :   *Values:*

            enumerator kDECODER\_ONLY[#](#_CPPv4N12tensorrt_llm8executor9ModelType13kDECODER_ONLYE "Link to this definition")

            enumerator kENCODER\_ONLY[#](#_CPPv4N12tensorrt_llm8executor9ModelType13kENCODER_ONLYE "Link to this definition")

            enumerator kENCODER\_DECODER[#](#_CPPv4N12tensorrt_llm8executor9ModelType16kENCODER_DECODERE "Link to this definition")

        enum class BatchingType[#](#_CPPv4N12tensorrt_llm8executor12BatchingTypeE "Link to this definition")
        :   The batching type.

            *Values:*

            enumerator kSTATIC[#](#_CPPv4N12tensorrt_llm8executor12BatchingType7kSTATICE "Link to this definition")
            :   STATIC refers to the traditional batching scheme with a batch of requests running in lockstep until the full generation for all of them is complete. Requests in a batch are all padded up to the maximum input and output sequence length of any member of the batch.

            enumerator kINFLIGHT[#](#_CPPv4N12tensorrt_llm8executor12BatchingType9kINFLIGHTE "Link to this definition")
            :   INFLIGHT refers to a scheme where newly arrived requests are dynamically incorporated into the batch under execution, and requests are returned as soon as the end condition is met without any padding.

        enum class CapacitySchedulerPolicy[#](#_CPPv4N12tensorrt_llm8executor23CapacitySchedulerPolicyE "Link to this definition")
        :   The policy used to select the subset of available requests in each iteration of the executor generation loop.

            *Values:*

            enumerator kMAX\_UTILIZATION[#](#_CPPv4N12tensorrt_llm8executor23CapacitySchedulerPolicy16kMAX_UTILIZATIONE "Link to this definition")
            :   MAX\_UTILIZATION packs as many requests as the underlying TRT engine can support in any iteration of the InflightBatching generation loop. While this is expected to maximize GPU throughput, it might require that some requests be paused and restarted depending on peak KV cache memory availability.

            enumerator kGUARANTEED\_NO\_EVICT[#](#_CPPv4N12tensorrt_llm8executor23CapacitySchedulerPolicy20kGUARANTEED_NO_EVICTE "Link to this definition")
            :   GUARANTEED\_NO\_EVICT uses KV cache more conservatively guaranteeing that a request, once started, will run to completion without eviction.

            enumerator kSTATIC\_BATCH[#](#_CPPv4N12tensorrt_llm8executor23CapacitySchedulerPolicy13kSTATIC_BATCHE "Link to this definition")
            :   kSTATIC\_BATCH does not schedule new requests until all requests in current batch are completed. Similar to kGUARANTEED\_NO\_EVICT, requests will run to completion without eviction.

        enum class ContextChunkingPolicy[#](#_CPPv4N12tensorrt_llm8executor21ContextChunkingPolicyE "Link to this definition")
        :   *Values:*

            enumerator kFIRST\_COME\_FIRST\_SERVED[#](#_CPPv4N12tensorrt_llm8executor21ContextChunkingPolicy24kFIRST_COME_FIRST_SERVEDE "Link to this definition")
            :   Sequential chunking, complete the unfinished context phase first.

            enumerator kEQUAL\_PROGRESS[#](#_CPPv4N12tensorrt_llm8executor21ContextChunkingPolicy15kEQUAL_PROGRESSE "Link to this definition")
            :   Iterate through each context request in sequence and attempt to increase its chunk count until the constraint is exceeded.

        enum class CommunicationType[#](#_CPPv4N12tensorrt_llm8executor17CommunicationTypeE "Link to this definition")
        :   *Values:*

            enumerator kMPI[#](#_CPPv4N12tensorrt_llm8executor17CommunicationType4kMPIE "Link to this definition")

        enum class CommunicationMode[#](#_CPPv4N12tensorrt_llm8executor17CommunicationModeE "Link to this definition")
        :   *Values:*

            enumerator kLEADER[#](#_CPPv4N12tensorrt_llm8executor17CommunicationMode7kLEADERE "Link to this definition")

            enumerator kORCHESTRATOR[#](#_CPPv4N12tensorrt_llm8executor17CommunicationMode13kORCHESTRATORE "Link to this definition")

        enum class RequestStage[#](#_CPPv4N12tensorrt_llm8executor12RequestStageE "Link to this definition")
        :   Enum class that represents the state of a request.

            *Values:*

            enumerator kQUEUED[#](#_CPPv4N12tensorrt_llm8executor12RequestStage7kQUEUEDE "Link to this definition")
            :   [Request](#classtensorrt__llm_1_1executor_1_1Request) that have been received but not yet included in the active requests (due to constraints such as maximum batch size for example).

            enumerator kENCODER\_IN\_PROGRESS[#](#_CPPv4N12tensorrt_llm8executor12RequestStage20kENCODER_IN_PROGRESSE "Link to this definition")
            :   Active request in encoder phase.

            enumerator kCONTEXT\_IN\_PROGRESS[#](#_CPPv4N12tensorrt_llm8executor12RequestStage20kCONTEXT_IN_PROGRESSE "Link to this definition")
            :   Active request in context phase.

            enumerator kGENERATION\_IN\_PROGRESS[#](#_CPPv4N12tensorrt_llm8executor12RequestStage23kGENERATION_IN_PROGRESSE "Link to this definition")
            :   Active request in generation phase.

            enumerator kGENERATION\_COMPLETE[#](#_CPPv4N12tensorrt_llm8executor12RequestStage20kGENERATION_COMPLETEE "Link to this definition")
            :   Active request for which generation has completed.

        enum class FinishReason[#](#_CPPv4N12tensorrt_llm8executor12FinishReasonE "Link to this definition")
        :   The reason why the model stopped generating tokens for a request.

            *Values:*

            enumerator kNOT\_FINISHED[#](#_CPPv4N12tensorrt_llm8executor12FinishReason13kNOT_FINISHEDE "Link to this definition")
            :   The request is not finished.

            enumerator kEND\_ID[#](#_CPPv4N12tensorrt_llm8executor12FinishReason7kEND_IDE "Link to this definition")
            :   The request finished because the end id was generated.

            enumerator kSTOP\_WORDS[#](#_CPPv4N12tensorrt_llm8executor12FinishReason11kSTOP_WORDSE "Link to this definition")
            :   The request finished because a stop word was generated.

            enumerator kLENGTH[#](#_CPPv4N12tensorrt_llm8executor12FinishReason7kLENGTHE "Link to this definition")
            :   The request finished because the maximum number of tokens was reached.

            enumerator kTIMED\_OUT[#](#_CPPv4N12tensorrt_llm8executor12FinishReason10kTIMED_OUTE "Link to this definition")
            :   The request finished because it got timed out (via the mAllotedTime parameter)

            enumerator kCANCELLED[#](#_CPPv4N12tensorrt_llm8executor12FinishReason10kCANCELLEDE "Link to this definition")
            :   The request was cancelled by calling cancelRequest.

        enum class KvCacheTransferMode[#](#_CPPv4N12tensorrt_llm8executor19KvCacheTransferModeE "Link to this definition")
        :   Enum describing the transfer mode for KV cache.

            *Values:*

            enumerator DRAM[#](#_CPPv4N12tensorrt_llm8executor19KvCacheTransferMode4DRAME "Link to this definition")
            :   Copy to/from CPU memory (original approach).

            enumerator GDS[#](#_CPPv4N12tensorrt_llm8executor19KvCacheTransferMode3GDSE "Link to this definition")
            :   Attempt GPUDirect Storage (cuFile).

            enumerator POSIX\_DEBUG\_FALLBACK[#](#_CPPv4N12tensorrt_llm8executor19KvCacheTransferMode20POSIX_DEBUG_FALLBACKE "Link to this definition")
            :   Force a POSIX read/write for debugging.

        Functions

        std::ostream &operator<<( : *std::ostream &os*, : *[CapacitySchedulerPolicy](#_CPPv4N12tensorrt_llm8executor23CapacitySchedulerPolicyE "tensorrt_llm::executor::CapacitySchedulerPolicy") policy*, )[#](#_CPPv4N12tensorrt_llm8executorlsERNSt7ostreamE23CapacitySchedulerPolicy "Link to this definition")

        std::ostream &operator<<( : *std::ostream &os*, : *[ContextChunkingPolicy](#_CPPv4N12tensorrt_llm8executor21ContextChunkingPolicyE "tensorrt_llm::executor::ContextChunkingPolicy") policy*, )[#](#_CPPv4N12tensorrt_llm8executorlsERNSt7ostreamE21ContextChunkingPolicy "Link to this definition")

        struct DebugTensorsPerIteration[#](#_CPPv4N12tensorrt_llm8executor24DebugTensorsPerIterationE "Link to this definition")
        :   *#include <types.h>*

            Struct that holds the debug tensors in an iteration.

            Public Members

            [IterationType](#_CPPv4N12tensorrt_llm8executor13IterationTypeE "tensorrt_llm::executor::IterationType") iter[#](#_CPPv4N12tensorrt_llm8executor24DebugTensorsPerIteration4iterE "Link to this definition")
            :   The iteration id for these tensors.

            std::map<std::string, [Tensor](#_CPPv4N12tensorrt_llm8executor6TensorE "tensorrt_llm::executor::Tensor")> debugTensors[#](#_CPPv4N12tensorrt_llm8executor24DebugTensorsPerIteration12debugTensorsE "Link to this definition")
            :   The debug tensors for this iteration.

        class DecodingMode[#](#_CPPv4N12tensorrt_llm8executor12DecodingModeE "Link to this definition")
        :   *#include <types.h>*

            mode of the decoder

            Public Types

            using UnderlyingType = uint32\_t[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "Link to this definition")

            Public Functions

            inline auto constexpr useTemperature(*bool useTemp*)[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode14useTemperatureEb "Link to this definition")

            inline auto constexpr useOccurrencePenalties(*bool usePenalty*)[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode22useOccurrencePenaltiesEb "Link to this definition")

            inline auto constexpr usePresencePenalty(*bool usePenalty*)[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode18usePresencePenaltyEb "Link to this definition")

            inline auto constexpr useRepetitionPenalty(*bool usePenalty*)[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode20useRepetitionPenaltyEb "Link to this definition")

            inline auto constexpr useFrequencyPenalty(*bool usePenalty*)[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode19useFrequencyPenaltyEb "Link to this definition")

            inline auto constexpr useMinLength(*bool useMinLen*)[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode12useMinLengthEb "Link to this definition")

            inline auto constexpr useBanTokens(*bool banTokens*)[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode12useBanTokensEb "Link to this definition")

            inline auto constexpr useBanWords(*bool banWords*)[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode11useBanWordsEb "Link to this definition")

            inline auto constexpr useNoRepeatNgramSize(*bool noRepeatNgramSize*)[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode20useNoRepeatNgramSizeEb "Link to this definition")

            inline auto constexpr useStopWords(*bool stopWords*)[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode12useStopWordsEb "Link to this definition")

            inline auto constexpr useMaxLengthStop(*bool maxLengthStop*)[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode16useMaxLengthStopEb "Link to this definition")

            inline auto constexpr useExplicitEosStop(*bool explicitEosStop*)[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode18useExplicitEosStopEb "Link to this definition")

            inline auto constexpr useMinP(*bool useMinP*)[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode7useMinPEb "Link to this definition")

            inline auto constexpr useVariableBeamWidthSearch( : *bool useVariableBeamWidthSearch*, )[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode26useVariableBeamWidthSearchEb "Link to this definition")

            inline bool constexpr isAuto() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode6isAutoEv "Link to this definition")

            inline bool constexpr isTopK() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode6isTopKEv "Link to this definition")

            inline bool constexpr isTopP() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode6isTopPEv "Link to this definition")

            inline bool constexpr isTopKorTopP() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode12isTopKorTopPEv "Link to this definition")

            inline bool constexpr isTopKandTopP() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode13isTopKandTopPEv "Link to this definition")

            inline bool constexpr isBeamSearch() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode12isBeamSearchEv "Link to this definition")

            inline bool constexpr isMedusa() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode8isMedusaEv "Link to this definition")

            inline bool constexpr isLookahead() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode11isLookaheadEv "Link to this definition")

            inline bool constexpr isExplicitDraftTokens() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode21isExplicitDraftTokensEv "Link to this definition")

            inline bool constexpr isExternalDraftTokens() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode21isExternalDraftTokensEv "Link to this definition")

            inline bool constexpr isEagle() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode7isEagleEv "Link to this definition")

            inline bool constexpr isUseTemperature() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode16isUseTemperatureEv "Link to this definition")

            inline bool constexpr isUsePresencePenalty() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode20isUsePresencePenaltyEv "Link to this definition")

            inline bool constexpr isUseFrequencyPenalty() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode21isUseFrequencyPenaltyEv "Link to this definition")

            inline bool constexpr isUseRepetitionPenalty() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode22isUseRepetitionPenaltyEv "Link to this definition")

            inline bool constexpr isUseMinLength() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode14isUseMinLengthEv "Link to this definition")

            inline bool constexpr isUseOccurrencePenalty() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode22isUseOccurrencePenaltyEv "Link to this definition")

            inline bool constexpr isUsePenalty() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode12isUsePenaltyEv "Link to this definition")

            inline bool constexpr isUseBanWords() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode13isUseBanWordsEv "Link to this definition")

            inline bool constexpr isUseNoRepeatNgramSize() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode22isUseNoRepeatNgramSizeEv "Link to this definition")

            inline bool constexpr isUseBanTokens() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode14isUseBanTokensEv "Link to this definition")

            inline bool constexpr isUseStopWords() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode14isUseStopWordsEv "Link to this definition")

            inline bool constexpr isUseMaxLengthStop() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode18isUseMaxLengthStopEv "Link to this definition")

            inline bool constexpr isUseExplicitEosStop() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode20isUseExplicitEosStopEv "Link to this definition")

            inline bool constexpr isUseStopCriteria() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode17isUseStopCriteriaEv "Link to this definition")

            inline bool constexpr isUseMinP() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode9isUseMinPEv "Link to this definition")

            inline bool constexpr isUseVariableBeamWidthSearch() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode28isUseVariableBeamWidthSearchEv "Link to this definition")

            inline bool operator==(*[DecodingMode](#_CPPv4N12tensorrt_llm8executor12DecodingModeE "tensorrt_llm::executor::DecodingMode") const &other*) const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingModeeqERK12DecodingMode "Link to this definition")

            inline explicit constexpr DecodingMode(*[UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") state*)[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode12DecodingModeE14UnderlyingType "Link to this definition")

            inline constexpr [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") getState() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode8getStateEv "Link to this definition")

            inline constexpr char const \*getName() const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode7getNameEv "Link to this definition")

            Public Static Functions

            static inline auto constexpr Auto()[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode4AutoEv "Link to this definition")
            :   No mode specified. Config will be determined from the beam width of the first request at runtime TopKTopP if beamWidth == 1, BeamSearch otherwise.

            static inline auto constexpr TopK()[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode4TopKEv "Link to this definition")

            static inline auto constexpr TopP()[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode4TopPEv "Link to this definition")

            static inline auto constexpr TopKTopP()[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode8TopKTopPEv "Link to this definition")

            static inline auto constexpr BeamSearch()[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode10BeamSearchEv "Link to this definition")

            static inline auto constexpr Medusa()[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode6MedusaEv "Link to this definition")

            static inline auto constexpr Lookahead()[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode9LookaheadEv "Link to this definition")

            static inline auto constexpr ExplicitDraftTokens()[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode19ExplicitDraftTokensEv "Link to this definition")

            static inline auto constexpr ExternalDraftTokens()[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode19ExternalDraftTokensEv "Link to this definition")

            static inline auto constexpr Eagle()[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode5EagleEv "Link to this definition")

            Private Functions

            inline bool constexpr anyBitSet(*[UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") bits*) const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode9anyBitSetE14UnderlyingType "Link to this definition")

            inline bool constexpr allBitSet(*[UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") bits*) const[#](#_CPPv4NK12tensorrt_llm8executor12DecodingMode9allBitSetE14UnderlyingType "Link to this definition")

            inline [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr setBitTo( : *[UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") state*, : *bool x*, )[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode8setBitToE14UnderlyingTypeb "Link to this definition")

            Private Members

            [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") mState = {}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode6mStateE "Link to this definition")

            Private Static Attributes

            static [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") constexpr kNumFlags = {12}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode9kNumFlagsE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kUseRepetitionPenalties = {1u << 0}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode23kUseRepetitionPenaltiesE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kUseFrequencyPenalties = {1u << 1}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode22kUseFrequencyPenaltiesE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kUsePresencePenalties = {1u << 2}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode21kUsePresencePenaltiesE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kUseTemperature = {1u << 3}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode15kUseTemperatureE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kUseMinLength = {1u << 4}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode13kUseMinLengthE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kUseBanWords = {1u << 5}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode12kUseBanWordsE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kUseStopWords = {1u << 6}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode13kUseStopWordsE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kUseMaxLengthStop = {1u << 7}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode17kUseMaxLengthStopE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kUseExplicitEosStop = {1u << 8}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode19kUseExplicitEosStopE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kUseNoRepeatNgramSize = {1u << 9}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode21kUseNoRepeatNgramSizeE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kUseMinP = {1u << 10}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode8kUseMinPE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kUseVariableBeamWidthSearch = {1u << 11}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode27kUseVariableBeamWidthSearchE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kUseStandardStopCriteria = {[kUseStopWords](#_CPPv4N12tensorrt_llm8executor12DecodingMode13kUseStopWordsE "tensorrt_llm::executor::DecodingMode::kUseStopWords") | [kUseMaxLengthStop](#_CPPv4N12tensorrt_llm8executor12DecodingMode17kUseMaxLengthStopE "tensorrt_llm::executor::DecodingMode::kUseMaxLengthStop")}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode24kUseStandardStopCriteriaE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kUseOccurrencePenalties{[kUseRepetitionPenalties](#_CPPv4N12tensorrt_llm8executor12DecodingMode23kUseRepetitionPenaltiesE "tensorrt_llm::executor::DecodingMode::kUseRepetitionPenalties") | [kUseFrequencyPenalties](#_CPPv4N12tensorrt_llm8executor12DecodingMode22kUseFrequencyPenaltiesE "tensorrt_llm::executor::DecodingMode::kUseFrequencyPenalties") | [kUsePresencePenalties](#_CPPv4N12tensorrt_llm8executor12DecodingMode21kUsePresencePenaltiesE "tensorrt_llm::executor::DecodingMode::kUsePresencePenalties")}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode23kUseOccurrencePenaltiesE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kUsePenalties = {[kUseOccurrencePenalties](#_CPPv4N12tensorrt_llm8executor12DecodingMode23kUseOccurrencePenaltiesE "tensorrt_llm::executor::DecodingMode::kUseOccurrencePenalties") | [kUseTemperature](#_CPPv4N12tensorrt_llm8executor12DecodingMode15kUseTemperatureE "tensorrt_llm::executor::DecodingMode::kUseTemperature") | [kUseMinLength](#_CPPv4N12tensorrt_llm8executor12DecodingMode13kUseMinLengthE "tensorrt_llm::executor::DecodingMode::kUseMinLength")}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode13kUsePenaltiesE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kUseBanTokens = {[kUseNoRepeatNgramSize](#_CPPv4N12tensorrt_llm8executor12DecodingMode21kUseNoRepeatNgramSizeE "tensorrt_llm::executor::DecodingMode::kUseNoRepeatNgramSize") | [kUseBanWords](#_CPPv4N12tensorrt_llm8executor12DecodingMode12kUseBanWordsE "tensorrt_llm::executor::DecodingMode::kUseBanWords")}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode13kUseBanTokensE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kAuto = {1u << ([kNumFlags](#_CPPv4N12tensorrt_llm8executor12DecodingMode9kNumFlagsE "tensorrt_llm::executor::DecodingMode::kNumFlags") + 0)}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode5kAutoE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kTopK = {1u << ([kNumFlags](#_CPPv4N12tensorrt_llm8executor12DecodingMode9kNumFlagsE "tensorrt_llm::executor::DecodingMode::kNumFlags") + 1)}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode5kTopKE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kTopP = {1u << ([kNumFlags](#_CPPv4N12tensorrt_llm8executor12DecodingMode9kNumFlagsE "tensorrt_llm::executor::DecodingMode::kNumFlags") + 2)}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode5kTopPE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kBeamSearch = {1u << ([kNumFlags](#_CPPv4N12tensorrt_llm8executor12DecodingMode9kNumFlagsE "tensorrt_llm::executor::DecodingMode::kNumFlags") + 3)}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode11kBeamSearchE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kMedusa = {1u << ([kNumFlags](#_CPPv4N12tensorrt_llm8executor12DecodingMode9kNumFlagsE "tensorrt_llm::executor::DecodingMode::kNumFlags") + 4)}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode7kMedusaE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kLookahead = {1u << ([kNumFlags](#_CPPv4N12tensorrt_llm8executor12DecodingMode9kNumFlagsE "tensorrt_llm::executor::DecodingMode::kNumFlags") + 5)}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode10kLookaheadE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kExplicitDraftTokens = {1u << ([kNumFlags](#_CPPv4N12tensorrt_llm8executor12DecodingMode9kNumFlagsE "tensorrt_llm::executor::DecodingMode::kNumFlags") + 6)}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode20kExplicitDraftTokensE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kExternalDraftTokens = {1u << ([kNumFlags](#_CPPv4N12tensorrt_llm8executor12DecodingMode9kNumFlagsE "tensorrt_llm::executor::DecodingMode::kNumFlags") + 7)}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode20kExternalDraftTokensE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kEagle = {1u << ([kNumFlags](#_CPPv4N12tensorrt_llm8executor12DecodingMode9kNumFlagsE "tensorrt_llm::executor::DecodingMode::kNumFlags") + 8)}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode6kEagleE "Link to this definition")

            static [UnderlyingType](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE "tensorrt_llm::executor::DecodingMode::UnderlyingType") constexpr kTopKTopP = {[kTopK](#_CPPv4N12tensorrt_llm8executor12DecodingMode5kTopKE "tensorrt_llm::executor::DecodingMode::kTopK") | [kTopP](#_CPPv4N12tensorrt_llm8executor12DecodingMode5kTopPE "tensorrt_llm::executor::DecodingMode::kTopP")}[#](#_CPPv4N12tensorrt_llm8executor12DecodingMode9kTopKTopPE "Link to this definition")

        struct DisServingRequestStats[#](#_CPPv4N12tensorrt_llm8executor22DisServingRequestStatsE "Link to this definition")
        :   *#include <types.h>*

            Struct that holds the request stats in the case of disaggregated serving.

            Public Members

            double kvCacheTransferMS[#](#_CPPv4N12tensorrt_llm8executor22DisServingRequestStats17kvCacheTransferMSE "Link to this definition")
            :   The total time spent on transferring KV cache from context phase to generation phase (ms)

            size\_t kvCacheSize[#](#_CPPv4N12tensorrt_llm8executor22DisServingRequestStats11kvCacheSizeE "Link to this definition")
            :   The total size of KV cache transferred from context phase to generation phase (bytes)

        struct InflightBatchingStats[#](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStatsE "Link to this definition")
        :   *#include <types.h>*

            Struct that holds the stats of inflight batching models for a single iteration.

            Public Members

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numScheduledRequests[#](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStats20numScheduledRequestsE "Link to this definition")
            :   Number of scheduled requests.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numContextRequests[#](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStats18numContextRequestsE "Link to this definition")
            :   Number of requests in context stage.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numGenRequests[#](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStats14numGenRequestsE "Link to this definition")
            :   Number of requests in generation stage.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numPausedRequests[#](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStats17numPausedRequestsE "Link to this definition")
            :   Number of paused requests.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numCtxTokens[#](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStats12numCtxTokensE "Link to this definition")
            :   Total number of context tokens in the iteration.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") microBatchId[#](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStats12microBatchIdE "Link to this definition")
            :   Index of mirco batch.

            float avgNumDecodedTokensPerIter[#](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStats26avgNumDecodedTokensPerIterE "Link to this definition")
            :   Average number of tokens decoded per request per iteration.

        struct IterationStats[#](#_CPPv4N12tensorrt_llm8executor14IterationStatsE "Link to this definition")
        :   *#include <types.h>*

            Struct that holds the stats of a single iteration.

            Public Members

            std::string timestamp[#](#_CPPv4N12tensorrt_llm8executor14IterationStats9timestampE "Link to this definition")
            :   Ending time of this iteration.

            [IterationType](#_CPPv4N12tensorrt_llm8executor13IterationTypeE "tensorrt_llm::executor::IterationType") iter[#](#_CPPv4N12tensorrt_llm8executor14IterationStats4iterE "Link to this definition")
            :   Iteration id.

            double iterLatencyMS[#](#_CPPv4N12tensorrt_llm8executor14IterationStats13iterLatencyMSE "Link to this definition")
            :   Iteration latency (ms)

            double newActiveRequestsQueueLatencyMS[#](#_CPPv4N12tensorrt_llm8executor14IterationStats31newActiveRequestsQueueLatencyMSE "Link to this definition")
            :   The total time spent in queue by the requests that became active in this iteration (ms)

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numNewActiveRequests[#](#_CPPv4N12tensorrt_llm8executor14IterationStats20numNewActiveRequestsE "Link to this definition")
            :   Number of new fetched active requests.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numActiveRequests[#](#_CPPv4N12tensorrt_llm8executor14IterationStats17numActiveRequestsE "Link to this definition")
            :   Number of active requests.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numQueuedRequests[#](#_CPPv4N12tensorrt_llm8executor14IterationStats17numQueuedRequestsE "Link to this definition")
            :   Number of queued requests.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numCompletedRequests[#](#_CPPv4N12tensorrt_llm8executor14IterationStats20numCompletedRequestsE "Link to this definition")
            :   Number of requests that were completed in this iteration.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") maxNumActiveRequests[#](#_CPPv4N12tensorrt_llm8executor14IterationStats20maxNumActiveRequestsE "Link to this definition")
            :   Number of max active requests.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") maxBatchSizeStatic[#](#_CPPv4N12tensorrt_llm8executor14IterationStats18maxBatchSizeStaticE "Link to this definition")
            :   Static max batch size passed to the executor.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") maxBatchSizeTunerRecommended[#](#_CPPv4N12tensorrt_llm8executor14IterationStats28maxBatchSizeTunerRecommendedE "Link to this definition")
            :   Batch size produced by dynamic tuner based on input stats.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") maxBatchSizeRuntime[#](#_CPPv4N12tensorrt_llm8executor14IterationStats19maxBatchSizeRuntimeE "Link to this definition")
            :   @brife The min of maxBatchSizeStatic and maxBatchSizeRuntimeUpperbound

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") maxNumTokensStatic[#](#_CPPv4N12tensorrt_llm8executor14IterationStats18maxNumTokensStaticE "Link to this definition")
            :   @brife Static max num tokens passed to the executor

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") maxNumTokensTunerRecommended[#](#_CPPv4N12tensorrt_llm8executor14IterationStats28maxNumTokensTunerRecommendedE "Link to this definition")
            :   @brife Max num tokens produced by dynamic tuner based on input stats

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") maxNumTokensRuntime[#](#_CPPv4N12tensorrt_llm8executor14IterationStats19maxNumTokensRuntimeE "Link to this definition")
            :   @brife The runtime max num tokens

            size\_t gpuMemUsage[#](#_CPPv4N12tensorrt_llm8executor14IterationStats11gpuMemUsageE "Link to this definition")
            :   GPU memory usage in bytes.

            size\_t cpuMemUsage[#](#_CPPv4N12tensorrt_llm8executor14IterationStats11cpuMemUsageE "Link to this definition")
            :   CPU memory usage in bytes.

            size\_t pinnedMemUsage[#](#_CPPv4N12tensorrt_llm8executor14IterationStats14pinnedMemUsageE "Link to this definition")
            :   Pinned memory usage in bytes.

            std::optional<[KvCacheStats](#_CPPv4N12tensorrt_llm8executor12KvCacheStatsE "tensorrt_llm::executor::KvCacheStats")> kvCacheStats[#](#_CPPv4N12tensorrt_llm8executor14IterationStats12kvCacheStatsE "Link to this definition")
            :   Stats specific to KV caches.

            std::optional<[KvCacheStats](#_CPPv4N12tensorrt_llm8executor12KvCacheStatsE "tensorrt_llm::executor::KvCacheStats")> crossKvCacheStats[#](#_CPPv4N12tensorrt_llm8executor14IterationStats17crossKvCacheStatsE "Link to this definition")
            :   Stats specific to cross KV caches.

            std::optional<[StaticBatchingStats](#_CPPv4N12tensorrt_llm8executor19StaticBatchingStatsE "tensorrt_llm::executor::StaticBatchingStats")> staticBatchingStats[#](#_CPPv4N12tensorrt_llm8executor14IterationStats19staticBatchingStatsE "Link to this definition")
            :   Stats specific to static batching.

            std::optional<[InflightBatchingStats](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStatsE "tensorrt_llm::executor::InflightBatchingStats")> inflightBatchingStats[#](#_CPPv4N12tensorrt_llm8executor14IterationStats21inflightBatchingStatsE "Link to this definition")
            :   Stats specific to inflight batching.

            std::optional<[SpecDecodingStats](#_CPPv4N12tensorrt_llm8executor17SpecDecodingStatsE "tensorrt_llm::executor::SpecDecodingStats")> specDecodingStats[#](#_CPPv4N12tensorrt_llm8executor14IterationStats17specDecodingStatsE "Link to this definition")
            :   Stats specific to speculative decoding.

        struct KvCacheStats[#](#_CPPv4N12tensorrt_llm8executor12KvCacheStatsE "Link to this definition")
        :   *#include <types.h>*

            Struct that holds the stats of a KV cache manager.

            Public Members

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") maxNumBlocks[#](#_CPPv4N12tensorrt_llm8executor12KvCacheStats12maxNumBlocksE "Link to this definition")
            :   Max number of blocks.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") freeNumBlocks[#](#_CPPv4N12tensorrt_llm8executor12KvCacheStats13freeNumBlocksE "Link to this definition")
            :   Number of free blocks.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") usedNumBlocks[#](#_CPPv4N12tensorrt_llm8executor12KvCacheStats13usedNumBlocksE "Link to this definition")
            :   Number of used blocks.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") tokensPerBlock[#](#_CPPv4N12tensorrt_llm8executor12KvCacheStats14tokensPerBlockE "Link to this definition")
            :   Number of tokens per block.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") allocTotalBlocks[#](#_CPPv4N12tensorrt_llm8executor12KvCacheStats16allocTotalBlocksE "Link to this definition")
            :   Number of total allocated block.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") allocNewBlocks[#](#_CPPv4N12tensorrt_llm8executor12KvCacheStats14allocNewBlocksE "Link to this definition")
            :   Number of newly allocated block.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") reusedBlocks[#](#_CPPv4N12tensorrt_llm8executor12KvCacheStats12reusedBlocksE "Link to this definition")
            :   Number of reused block.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") missedBlocks[#](#_CPPv4N12tensorrt_llm8executor12KvCacheStats12missedBlocksE "Link to this definition")
            :   Number of not reused block.

            float cacheHitRate[#](#_CPPv4N12tensorrt_llm8executor12KvCacheStats12cacheHitRateE "Link to this definition")
            :   Measuring the KV Cache reuse rate. cacheHitRate = reusedBlocks / (reusedBlocks + missedBlocks).

        struct RequestPerfMetrics[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetricsE "Link to this definition")
        :   *#include <types.h>*

            Struct that holds the stats of a request.

            Public Types

            using TimePoint = std::chrono::time\_point<std::chrono::steady\_clock>[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics9TimePointE "Link to this definition")

            Public Members

            [TimingMetrics](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13TimingMetricsE "tensorrt_llm::executor::RequestPerfMetrics::TimingMetrics") timingMetrics[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13timingMetricsE "Link to this definition")

            [KvCacheMetrics](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics14KvCacheMetricsE "tensorrt_llm::executor::RequestPerfMetrics::KvCacheMetrics") kvCacheMetrics[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics14kvCacheMetricsE "Link to this definition")

            [SpeculativeDecodingMetrics](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics26SpeculativeDecodingMetricsE "tensorrt_llm::executor::RequestPerfMetrics::SpeculativeDecodingMetrics") speculativeDecoding[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics19speculativeDecodingE "Link to this definition")

            std::optional<[IterationType](#_CPPv4N12tensorrt_llm8executor13IterationTypeE "tensorrt_llm::executor::IterationType")> firstIter[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics9firstIterE "Link to this definition")
            :   First iteration where the request was processed.

            std::optional<[IterationType](#_CPPv4N12tensorrt_llm8executor13IterationTypeE "tensorrt_llm::executor::IterationType")> lastIter[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics8lastIterE "Link to this definition")
            :   Last iteration where a token was generated.

            std::optional<[IterationType](#_CPPv4N12tensorrt_llm8executor13IterationTypeE "tensorrt_llm::executor::IterationType")> iter[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics4iterE "Link to this definition")
            :   Current iteration.

            struct KvCacheMetrics[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics14KvCacheMetricsE "Link to this definition")
            :   Public Members

                [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numTotalAllocatedBlocks = {0}[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics14KvCacheMetrics23numTotalAllocatedBlocksE "Link to this definition")
                :   Number of total allocated blocks.

                [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numNewAllocatedBlocks = {0}[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics14KvCacheMetrics21numNewAllocatedBlocksE "Link to this definition")
                :   Number of newly allocated blocks.

                [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numReusedBlocks = {0}[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics14KvCacheMetrics15numReusedBlocksE "Link to this definition")
                :   Number of reused blocks.

                [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numMissedBlocks = {0}[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics14KvCacheMetrics15numMissedBlocksE "Link to this definition")
                :   Number of missed blocks.

                [FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType") kvCacheHitRate = {0.f}[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics14KvCacheMetrics14kvCacheHitRateE "Link to this definition")
                :   KV Cache Hit Rate, defined as reusedBlocks / (reusedBlocks + missedBlocks)

            struct SpeculativeDecodingMetrics[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics26SpeculativeDecodingMetricsE "Link to this definition")
            :   Public Members

                [FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType") acceptanceRate = {0.f}[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics26SpeculativeDecodingMetrics14acceptanceRateE "Link to this definition")
                :   Token acceptance rate for speculative decoding requests.

                [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") totalAcceptedDraftTokens = {0}[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics26SpeculativeDecodingMetrics24totalAcceptedDraftTokensE "Link to this definition")
                :   Total number of accepted draft tokens.

                [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") totalDraftTokens = {0}[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics26SpeculativeDecodingMetrics16totalDraftTokensE "Link to this definition")
                :   Total number of draft tokens used in the request.

            struct TimingMetrics[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13TimingMetricsE "Link to this definition")
            :   Public Members

                [TimePoint](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics9TimePointE "tensorrt_llm::executor::RequestPerfMetrics::TimePoint") arrivalTime[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13TimingMetrics11arrivalTimeE "Link to this definition")
                :   The time when the request arrived.

                [TimePoint](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics9TimePointE "tensorrt_llm::executor::RequestPerfMetrics::TimePoint") firstScheduledTime[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13TimingMetrics18firstScheduledTimeE "Link to this definition")
                :   The time when the request was first scheduled.

                [TimePoint](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics9TimePointE "tensorrt_llm::executor::RequestPerfMetrics::TimePoint") firstTokenTime[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13TimingMetrics14firstTokenTimeE "Link to this definition")
                :   The time when the first token was generated.

                [TimePoint](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics9TimePointE "tensorrt_llm::executor::RequestPerfMetrics::TimePoint") lastTokenTime[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13TimingMetrics13lastTokenTimeE "Link to this definition")
                :   The time when the request was finished.

                [TimePoint](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics9TimePointE "tensorrt_llm::executor::RequestPerfMetrics::TimePoint") kvCacheTransferStart[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13TimingMetrics20kvCacheTransferStartE "Link to this definition")
                :   Start time of the KV cache transfer for disaggregated serving.

                [TimePoint](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics9TimePointE "tensorrt_llm::executor::RequestPerfMetrics::TimePoint") kvCacheTransferEnd[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13TimingMetrics18kvCacheTransferEndE "Link to this definition")
                :   End time of the KV cache transfer for disaggregated serving.

                mutable size\_t kvCacheSize = 0[#](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13TimingMetrics11kvCacheSizeE "Link to this definition")
                :   KV Cache size transfer for disaggregated serving.

        struct RequestStats[#](#_CPPv4N12tensorrt_llm8executor12RequestStatsE "Link to this definition")
        :   *#include <types.h>*

            Struct that holds the stats of a single request.

            Public Members

            [IdType](#_CPPv4N12tensorrt_llm8executor6IdTypeE "tensorrt_llm::executor::IdType") id[#](#_CPPv4N12tensorrt_llm8executor12RequestStats2idE "Link to this definition")
            :   The request id.

            [RequestStage](#_CPPv4N12tensorrt_llm8executor12RequestStageE "tensorrt_llm::executor::RequestStage") stage[#](#_CPPv4N12tensorrt_llm8executor12RequestStats5stageE "Link to this definition")
            :   The current stage the request is in.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") contextPrefillPosition[#](#_CPPv4N12tensorrt_llm8executor12RequestStats22contextPrefillPositionE "Link to this definition")
            :   If using chunked context, the current context prefill position.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numGeneratedTokens[#](#_CPPv4N12tensorrt_llm8executor12RequestStats18numGeneratedTokensE "Link to this definition")
            :   The number of generated tokens so far.

            float avgNumDecodedTokensPerIter[#](#_CPPv4N12tensorrt_llm8executor12RequestStats26avgNumDecodedTokensPerIterE "Link to this definition")
            :   The average number of decoded tokens per iteration. It is >= 1 for speculative decoding.

            bool scheduled[#](#_CPPv4N12tensorrt_llm8executor12RequestStats9scheduledE "Link to this definition")
            :   Whether the request is scheduled for the current iteration.

            bool paused[#](#_CPPv4N12tensorrt_llm8executor12RequestStats6pausedE "Link to this definition")
            :   Whether the request is being paused at the current iteration due to lack of resources (KV cache blocks exhaustion for example)

            std::optional<[DisServingRequestStats](#_CPPv4N12tensorrt_llm8executor22DisServingRequestStatsE "tensorrt_llm::executor::DisServingRequestStats")> disServingStats[#](#_CPPv4N12tensorrt_llm8executor12RequestStats15disServingStatsE "Link to this definition")
            :   Stats specific to disaggregated serving.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") allocTotalBlocksPerRequest[#](#_CPPv4N12tensorrt_llm8executor12RequestStats26allocTotalBlocksPerRequestE "Link to this definition")
            :   Number of total allocated blocks per request.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") allocNewBlocksPerRequest[#](#_CPPv4N12tensorrt_llm8executor12RequestStats24allocNewBlocksPerRequestE "Link to this definition")
            :   Number of newly allocated blocks per request.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") reusedBlocksPerRequest[#](#_CPPv4N12tensorrt_llm8executor12RequestStats22reusedBlocksPerRequestE "Link to this definition")
            :   Number of reused blocks per request.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") missedBlocksPerRequest[#](#_CPPv4N12tensorrt_llm8executor12RequestStats22missedBlocksPerRequestE "Link to this definition")
            :   Number of missed blocks per request.

            [FloatType](#_CPPv4N12tensorrt_llm8executor9FloatTypeE "tensorrt_llm::executor::FloatType") kvCacheHitRatePerRequest[#](#_CPPv4N12tensorrt_llm8executor12RequestStats24kvCacheHitRatePerRequestE "Link to this definition")
            :   KV Cache Hit Rate per request, defined as reusedBlocks / (reusedBlocks + missedBlocks)

        struct RequestStatsPerIteration[#](#_CPPv4N12tensorrt_llm8executor24RequestStatsPerIterationE "Link to this definition")
        :   *#include <types.h>*

            Struct that holds the stats of all requests in an iteration.

            Public Members

            [IterationType](#_CPPv4N12tensorrt_llm8executor13IterationTypeE "tensorrt_llm::executor::IterationType") iter[#](#_CPPv4N12tensorrt_llm8executor24RequestStatsPerIteration4iterE "Link to this definition")
            :   The iteration id for these stats.

            std::vector<[RequestStats](#_CPPv4N12tensorrt_llm8executor12RequestStatsE "tensorrt_llm::executor::RequestStats")> requestStats[#](#_CPPv4N12tensorrt_llm8executor24RequestStatsPerIteration12requestStatsE "Link to this definition")
            :   The stats of all active requests for this iteration.

        struct SpecDecodingStats[#](#_CPPv4N12tensorrt_llm8executor17SpecDecodingStatsE "Link to this definition")
        :   *#include <types.h>*

            Struct that holds speculative decoding stats.

            Public Members

            [SizeType64](#_CPPv4N12tensorrt_llm8executor10SizeType64E "tensorrt_llm::executor::SizeType64") numDraftTokens[#](#_CPPv4N12tensorrt_llm8executor17SpecDecodingStats14numDraftTokensE "Link to this definition")
            :   Total number of proposed draft tokens for all requests.

            [SizeType64](#_CPPv4N12tensorrt_llm8executor10SizeType64E "tensorrt_llm::executor::SizeType64") numAcceptedTokens[#](#_CPPv4N12tensorrt_llm8executor17SpecDecodingStats17numAcceptedTokensE "Link to this definition")
            :   Total number of accepted draft tokens for all requests.

            [SizeType64](#_CPPv4N12tensorrt_llm8executor10SizeType64E "tensorrt_llm::executor::SizeType64") numRequestsWithDraftTokens[#](#_CPPv4N12tensorrt_llm8executor17SpecDecodingStats26numRequestsWithDraftTokensE "Link to this definition")
            :   Number of requests with at least one draft token in batch.

            double acceptanceLength[#](#_CPPv4N12tensorrt_llm8executor17SpecDecodingStats16acceptanceLengthE "Link to this definition")
            :   Acceptance length, defined as average number of tokens produced per step for all requests with at least one draft token.

            double iterLatencyMS[#](#_CPPv4N12tensorrt_llm8executor17SpecDecodingStats13iterLatencyMSE "Link to this definition")
            :   Iteration latency for draft token generation only (ms)

            double draftOverhead[#](#_CPPv4N12tensorrt_llm8executor17SpecDecodingStats13draftOverheadE "Link to this definition")
            :   Draft overhead, defined as iterLatencyMS (specdec) / iterLatencyMS (total)

        struct StaticBatchingStats[#](#_CPPv4N12tensorrt_llm8executor19StaticBatchingStatsE "Link to this definition")
        :   *#include <types.h>*

            Struct that holds the stats of static batching models for a single iteration.

            Public Members

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numScheduledRequests[#](#_CPPv4N12tensorrt_llm8executor19StaticBatchingStats20numScheduledRequestsE "Link to this definition")
            :   Number of scheduled requests.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numContextRequests[#](#_CPPv4N12tensorrt_llm8executor19StaticBatchingStats18numContextRequestsE "Link to this definition")
            :   Number of requests in context stage.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numCtxTokens[#](#_CPPv4N12tensorrt_llm8executor19StaticBatchingStats12numCtxTokensE "Link to this definition")
            :   Total number of context tokens in the iteration.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") numGenTokens[#](#_CPPv4N12tensorrt_llm8executor19StaticBatchingStats12numGenTokensE "Link to this definition")
            :   Total number of tokens to generate in the iteration.

            [SizeType32](#_CPPv4N12tensorrt_llm8executor10SizeType32E "tensorrt_llm::executor::SizeType32") emptyGenSlots[#](#_CPPv4N12tensorrt_llm8executor19StaticBatchingStats13emptyGenSlotsE "Link to this definition")
            :   Total number of unused generation token slots.

        template<typename T, bool = false> struct TypeTraits[#](#_CPPv4I0_bEN12tensorrt_llm8executor10TypeTraitsE "Link to this definition")
        :   *#include <types.h>*

            For converting a C++ data type to a `TrtLmmDataType`.

        template<> struct TypeTraits<bool>[#](#_CPPv4IEN12tensorrt_llm8executor10TypeTraitsIbEE "Link to this definition")
        :   Public Static Attributes

            static constexpr auto value = [DataType](#_CPPv4N12tensorrt_llm8executor8DataTypeE "tensorrt_llm::executor::DataType")::[kBOOL](#_CPPv4N12tensorrt_llm8executor8DataType5kBOOLE "tensorrt_llm::executor::DataType::kBOOL")[#](#_CPPv4N12tensorrt_llm8executor10TypeTraitsIbE5valueE "Link to this definition")

        template<> struct TypeTraits<float>[#](#_CPPv4IEN12tensorrt_llm8executor10TypeTraitsIfEE "Link to this definition")
        :   Public Static Attributes

            static constexpr auto value = [DataType](#_CPPv4N12tensorrt_llm8executor8DataTypeE "tensorrt_llm::executor::DataType")::[kFP32](#_CPPv4N12tensorrt_llm8executor8DataType5kFP32E "tensorrt_llm::executor::DataType::kFP32")[#](#_CPPv4N12tensorrt_llm8executor10TypeTraitsIfE5valueE "Link to this definition")

        template<> struct TypeTraits<half>[#](#_CPPv4IEN12tensorrt_llm8executor10TypeTraitsI4halfEE "Link to this definition")
        :   Public Static Attributes

            static constexpr auto value = [DataType](#_CPPv4N12tensorrt_llm8executor8DataTypeE "tensorrt_llm::executor::DataType")::[kFP16](#_CPPv4N12tensorrt_llm8executor8DataType5kFP16E "tensorrt_llm::executor::DataType::kFP16")[#](#_CPPv4N12tensorrt_llm8executor10TypeTraitsI4halfE5valueE "Link to this definition")

        template<> struct TypeTraits<std::int32\_t>[#](#_CPPv4IEN12tensorrt_llm8executor10TypeTraitsINSt7int32_tEEE "Link to this definition")
        :   Public Static Attributes

            static constexpr auto value = [DataType](#_CPPv4N12tensorrt_llm8executor8DataTypeE "tensorrt_llm::executor::DataType")::[kINT32](#_CPPv4N12tensorrt_llm8executor8DataType6kINT32E "tensorrt_llm::executor::DataType::kINT32")[#](#_CPPv4N12tensorrt_llm8executor10TypeTraitsINSt7int32_tEE5valueE "Link to this definition")

        template<> struct TypeTraits<std::int64\_t>[#](#_CPPv4IEN12tensorrt_llm8executor10TypeTraitsINSt7int64_tEEE "Link to this definition")
        :   Public Static Attributes

            static constexpr auto value = [DataType](#_CPPv4N12tensorrt_llm8executor8DataTypeE "tensorrt_llm::executor::DataType")::[kINT64](#_CPPv4N12tensorrt_llm8executor8DataType6kINT64E "tensorrt_llm::executor::DataType::kINT64")[#](#_CPPv4N12tensorrt_llm8executor10TypeTraitsINSt7int64_tEE5valueE "Link to this definition")

        template<> struct TypeTraits<std::int8\_t>[#](#_CPPv4IEN12tensorrt_llm8executor10TypeTraitsINSt6int8_tEEE "Link to this definition")
        :   Public Static Attributes

            static constexpr auto value = [DataType](#_CPPv4N12tensorrt_llm8executor8DataTypeE "tensorrt_llm::executor::DataType")::[kINT8](#_CPPv4N12tensorrt_llm8executor8DataType5kINT8E "tensorrt_llm::executor::DataType::kINT8")[#](#_CPPv4N12tensorrt_llm8executor10TypeTraitsINSt6int8_tEE5valueE "Link to this definition")

        template<> struct TypeTraits<std::uint8\_t>[#](#_CPPv4IEN12tensorrt_llm8executor10TypeTraitsINSt7uint8_tEEE "Link to this definition")
        :   Public Static Attributes

            static constexpr auto value = [DataType](#_CPPv4N12tensorrt_llm8executor8DataTypeE "tensorrt_llm::executor::DataType")::[kUINT8](#_CPPv4N12tensorrt_llm8executor8DataType6kUINT8E "tensorrt_llm::executor::DataType::kUINT8")[#](#_CPPv4N12tensorrt_llm8executor10TypeTraitsINSt7uint8_tEE5valueE "Link to this definition")

        template<typename T> struct TypeTraits<[T](#_CPPv4I0EN12tensorrt_llm8executor10TypeTraitsIP1TEE "tensorrt_llm::executor::TypeTraits<T*>::T")\*>[#](#_CPPv4I0EN12tensorrt_llm8executor10TypeTraitsIP1TEE "Link to this definition")
        :   Public Static Attributes

            static constexpr auto value = [DataType](#_CPPv4N12tensorrt_llm8executor8DataTypeE "tensorrt_llm::executor::DataType")::[kINT64](#_CPPv4N12tensorrt_llm8executor8DataType6kINT64E "tensorrt_llm::executor::DataType::kINT64")[#](#_CPPv4N12tensorrt_llm8executor10TypeTraitsIP1TE5valueE "Link to this definition")

    namespace runtime

On this page

* [cacheCommunicator.h](#cachecommunicator-h)
  + [`tensorrt_llm`](#_CPPv412tensorrt_llm)
    - [`tensorrt_llm::executor`](#_CPPv4N12tensorrt_llm8executorE)
      * [`tensorrt_llm::executor::kv_cache`](#_CPPv4N12tensorrt_llm8executor8kv_cacheE)
        + [`tensorrt_llm::executor::kv_cache::Connection`](#_CPPv4N12tensorrt_llm8executor8kv_cache10ConnectionE)
          - [`~Connection()`](#_CPPv4N12tensorrt_llm8executor8kv_cache10ConnectionD0Ev)
          - [`send()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache10Connection4sendERK11DataContextPKv6size_t)
          - [`recv()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache10Connection4recvERK11DataContextPv6size_t)
          - [`isThreadSafe()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache10Connection12isThreadSafeEv)
        + [`tensorrt_llm::executor::kv_cache::ConnectionManager`](#_CPPv4N12tensorrt_llm8executor8kv_cache17ConnectionManagerE)
          - [`~ConnectionManager()`](#_CPPv4N12tensorrt_llm8executor8kv_cache17ConnectionManagerD0Ev)
          - [`recvConnect()`](#_CPPv4N12tensorrt_llm8executor8kv_cache17ConnectionManager11recvConnectERK11DataContextPv6size_t)
          - [`getConnections()`](#_CPPv4N12tensorrt_llm8executor8kv_cache17ConnectionManager14getConnectionsERK9CommState)
          - [`getCommState()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache17ConnectionManager12getCommStateEv)
        + [`tensorrt_llm::executor::kv_cache::DataContext`](#_CPPv4N12tensorrt_llm8executor8kv_cache11DataContextE)
          - [`DataContext()`](#_CPPv4N12tensorrt_llm8executor8kv_cache11DataContext11DataContextEi)
          - [`getTag()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache11DataContext6getTagEv)
          - [`mTag`](#_CPPv4N12tensorrt_llm8executor8kv_cache11DataContext4mTagE)
* [serialization.h](#serialization-h)
  + [`tensorrt_llm::executor::Serialization`](#_CPPv4N12tensorrt_llm8executor13SerializationE)
    - [`deserializeTimePoint()`](#_CPPv4N12tensorrt_llm8executor13Serialization20deserializeTimePointERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKN18RequestPerfMetrics9TimePointERNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERKN18RequestPerfMetrics9TimePointE)
    - [`deserializeRequestPerfMetrics()`](#_CPPv4N12tensorrt_llm8executor13Serialization29deserializeRequestPerfMetricsERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK18RequestPerfMetricsRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK18RequestPerfMetrics)
    - [`deserializeSamplingConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization25deserializeSamplingConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK14SamplingConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK14SamplingConfig)
    - [`deserializeOutputConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization23deserializeOutputConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK12OutputConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK12OutputConfig)
    - [`deserializeAdditionalModelOutput()`](#_CPPv4N12tensorrt_llm8executor13Serialization32deserializeAdditionalModelOutputERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK21AdditionalModelOutputRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK21AdditionalModelOutput)
    - [`deserializeExternalDraftTokensConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization36deserializeExternalDraftTokensConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK25ExternalDraftTokensConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK25ExternalDraftTokensConfig)
    - [`deserializePromptTuningConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization29deserializePromptTuningConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK18PromptTuningConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK18PromptTuningConfig)
    - [`deserializeMultimodalInput()`](#_CPPv4N12tensorrt_llm8executor13Serialization26deserializeMultimodalInputERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK15MultimodalInputRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK15MultimodalInput)
    - [`deserializeMropeConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization22deserializeMropeConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK11MropeConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK11MropeConfig)
    - [`deserializeLoraConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization21deserializeLoraConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK10LoraConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK10LoraConfig)
    - [`deserializeCommState()`](#_CPPv4N12tensorrt_llm8executor13Serialization20deserializeCommStateERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKN8kv_cache9CommStateERNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERKN8kv_cache9CommStateE)
    - [`deserializeSocketState()`](#_CPPv4N12tensorrt_llm8executor13Serialization22deserializeSocketStateERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKN8kv_cache11SocketStateERNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERKN8kv_cache11SocketStateE)
    - [`deserializeAgentState()`](#_CPPv4N12tensorrt_llm8executor13Serialization21deserializeAgentStateERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKN8kv_cache10AgentStateERNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERKN8kv_cache10AgentStateE)
    - [`deserializeCacheState()`](#_CPPv4N12tensorrt_llm8executor13Serialization21deserializeCacheStateERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKN8kv_cache10CacheStateERNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERKN8kv_cache10CacheStateE)
    - [`deserializeDataTransceiverState()`](#_CPPv4N12tensorrt_llm8executor13Serialization31deserializeDataTransceiverStateERNSt7istreamE)
    - [`deserializeDataTransceiverState()`](#_CPPv4N12tensorrt_llm8executor13Serialization31deserializeDataTransceiverStateERNSt6vectorIcEE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK20DataTransceiverStateRNSt7ostreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK20DataTransceiverState)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK20DataTransceiverState)
    - [`deserializeContextPhaseParams()`](#_CPPv4N12tensorrt_llm8executor13Serialization29deserializeContextPhaseParamsERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK18ContextPhaseParamsRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK18ContextPhaseParams)
    - [`deserializeRequest()`](#_CPPv4N12tensorrt_llm8executor13Serialization18deserializeRequestERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK7RequestRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK7Request)
    - [`deserializeTensor()`](#_CPPv4N12tensorrt_llm8executor13Serialization17deserializeTensorERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK6TensorRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK6Tensor)
    - [`deserializeSpecDecFastLogitsInfo()`](#_CPPv4N12tensorrt_llm8executor13Serialization32deserializeSpecDecFastLogitsInfoERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK33SpeculativeDecodingFastLogitsInfoRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK33SpeculativeDecodingFastLogitsInfo)
    - [`deserializeResult()`](#_CPPv4N12tensorrt_llm8executor13Serialization17deserializeResultERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK6ResultRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK6Result)
    - [`deserializeAdditionalOutput()`](#_CPPv4N12tensorrt_llm8executor13Serialization27deserializeAdditionalOutputERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK16AdditionalOutputRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK16AdditionalOutput)
    - [`deserializeResponse()`](#_CPPv4N12tensorrt_llm8executor13Serialization19deserializeResponseERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK8ResponseRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK8Response)
    - [`deserializeResponses()`](#_CPPv4N12tensorrt_llm8executor13Serialization20deserializeResponsesERNSt6vectorIcEE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKNSt6vectorI8ResponseEE)
    - [`deserializeKvCacheConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization24deserializeKvCacheConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK13KvCacheConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK13KvCacheConfig)
    - [`deserializeDynamicBatchConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization29deserializeDynamicBatchConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK18DynamicBatchConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK18DynamicBatchConfig)
    - [`deserializeSchedulerConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization26deserializeSchedulerConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK15SchedulerConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK15SchedulerConfig)
    - [`deserializeExtendedRuntimePerfKnobConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization40deserializeExtendedRuntimePerfKnobConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK29ExtendedRuntimePerfKnobConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK29ExtendedRuntimePerfKnobConfig)
    - [`deserializeParallelConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization25deserializeParallelConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK14ParallelConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK14ParallelConfig)
    - [`deserializePeftCacheConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization26deserializePeftCacheConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK15PeftCacheConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK15PeftCacheConfig)
    - [`deserializeOrchestratorConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization29deserializeOrchestratorConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK18OrchestratorConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK18OrchestratorConfig)
    - [`deserializeDecodingMode()`](#_CPPv4N12tensorrt_llm8executor13Serialization23deserializeDecodingModeERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK12DecodingModeRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK12DecodingMode)
    - [`deserializeLookaheadDecodingConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization34deserializeLookaheadDecodingConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK23LookaheadDecodingConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK23LookaheadDecodingConfig)
    - [`deserializeEagleConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization22deserializeEagleConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK11EagleConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK11EagleConfig)
    - [`deserializeSpeculativeDecodingConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization36deserializeSpeculativeDecodingConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK25SpeculativeDecodingConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK25SpeculativeDecodingConfig)
    - [`deserializeGuidedDecodingConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization31deserializeGuidedDecodingConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK20GuidedDecodingConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK20GuidedDecodingConfig)
    - [`deserializeGuidedDecodingParams()`](#_CPPv4N12tensorrt_llm8executor13Serialization31deserializeGuidedDecodingParamsERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK20GuidedDecodingParamsRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK20GuidedDecodingParams)
    - [`deserializeKvCacheRetentionConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization33deserializeKvCacheRetentionConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK22KvCacheRetentionConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK22KvCacheRetentionConfig)
    - [`deserializeTokenRangeRetentionConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization36deserializeTokenRangeRetentionConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKN22KvCacheRetentionConfig25TokenRangeRetentionConfigERNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERKN22KvCacheRetentionConfig25TokenRangeRetentionConfigE)
    - [`deserializeDecodingConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization25deserializeDecodingConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK14DecodingConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK14DecodingConfig)
    - [`deserializeDebugConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization22deserializeDebugConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK11DebugConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK11DebugConfig)
    - [`deserializeCacheTransceiverConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization33deserializeCacheTransceiverConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK22CacheTransceiverConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK22CacheTransceiverConfig)
    - [`deserializeExecutorConfig()`](#_CPPv4N12tensorrt_llm8executor13Serialization25deserializeExecutorConfigERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK14ExecutorConfigRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK14ExecutorConfig)
    - [`deserializeKvCacheStats()`](#_CPPv4N12tensorrt_llm8executor13Serialization23deserializeKvCacheStatsERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK12KvCacheStatsRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK12KvCacheStats)
    - [`deserializeStaticBatchingStats()`](#_CPPv4N12tensorrt_llm8executor13Serialization30deserializeStaticBatchingStatsERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK19StaticBatchingStatsRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK19StaticBatchingStats)
    - [`deserializeInflightBatchingStats()`](#_CPPv4N12tensorrt_llm8executor13Serialization32deserializeInflightBatchingStatsERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK21InflightBatchingStatsRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK21InflightBatchingStats)
    - [`deserializeSpecDecodingStats()`](#_CPPv4N12tensorrt_llm8executor13Serialization28deserializeSpecDecodingStatsERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK17SpecDecodingStatsRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK17SpecDecodingStats)
    - [`deserializeIterationStats()`](#_CPPv4N12tensorrt_llm8executor13Serialization25deserializeIterationStatsERNSt6vectorIcEE)
    - [`deserializeIterationStats()`](#_CPPv4N12tensorrt_llm8executor13Serialization25deserializeIterationStatsERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK14IterationStatsRNSt7ostreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK14IterationStats)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK14IterationStats)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKNSt6vectorI14IterationStatsEE)
    - [`deserializeIterationStatsVec()`](#_CPPv4N12tensorrt_llm8executor13Serialization28deserializeIterationStatsVecERNSt6vectorIcEE)
    - [`deserializeDisServingRequestStats()`](#_CPPv4N12tensorrt_llm8executor13Serialization33deserializeDisServingRequestStatsERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK22DisServingRequestStatsRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK22DisServingRequestStats)
    - [`deserializeRequestStage()`](#_CPPv4N12tensorrt_llm8executor13Serialization23deserializeRequestStageERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK12RequestStageRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK12RequestStage)
    - [`deserializeRequestStats()`](#_CPPv4N12tensorrt_llm8executor13Serialization23deserializeRequestStatsERNSt7istreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK12RequestStatsRNSt7ostreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK12RequestStats)
    - [`deserializeRequestStatsPerIteration()`](#_CPPv4N12tensorrt_llm8executor13Serialization35deserializeRequestStatsPerIterationERNSt7istreamE)
    - [`deserializeRequestStatsPerIteration()`](#_CPPv4N12tensorrt_llm8executor13Serialization35deserializeRequestStatsPerIterationERNSt6vectorIcEE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK24RequestStatsPerIterationRNSt7ostreamE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK24RequestStatsPerIteration)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK24RequestStatsPerIteration)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKNSt6vectorI24RequestStatsPerIterationEE)
    - [`deserializeRequestStatsPerIterationVec()`](#_CPPv4N12tensorrt_llm8executor13Serialization38deserializeRequestStatsPerIterationVecERNSt6vectorIcEE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKNSt5dequeI12KVCacheEventEE)
    - [`deserializeKVCacheEvents()`](#_CPPv4N12tensorrt_llm8executor13Serialization24deserializeKVCacheEventsERNSt6vectorIcEE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK12KVCacheEvent)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK12KVCacheEventRNSt7ostreamE)
    - [`deserializeKVCacheEvent()`](#_CPPv4N12tensorrt_llm8executor13Serialization23deserializeKVCacheEventERNSt7istreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK18KVCacheCreatedData)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK18KVCacheCreatedDataRNSt7ostreamE)
    - [`deserializeKVCacheCreatedData()`](#_CPPv4N12tensorrt_llm8executor13Serialization29deserializeKVCacheCreatedDataERNSt7istreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK17KVCacheStoredData)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK17KVCacheStoredDataRNSt7ostreamE)
    - [`deserializeKVCacheStoredData()`](#_CPPv4N12tensorrt_llm8executor13Serialization28deserializeKVCacheStoredDataERNSt7istreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK22KVCacheStoredBlockData)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK22KVCacheStoredBlockDataRNSt7ostreamE)
    - [`deserializeKVCacheStoredBlockData()`](#_CPPv4N12tensorrt_llm8executor13Serialization33deserializeKVCacheStoredBlockDataERNSt7istreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK18KVCacheRemovedData)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK18KVCacheRemovedDataRNSt7ostreamE)
    - [`deserializeKVCacheRemovedData()`](#_CPPv4N12tensorrt_llm8executor13Serialization29deserializeKVCacheRemovedDataERNSt7istreamE)
    - [`serializedSize()`](#_CPPv4I0EN12tensorrt_llm8executor13Serialization14serializedSizeE6size_tRK16KVCacheEventDiffI1TE)
    - [`serialize()`](#_CPPv4I0EN12tensorrt_llm8executor13Serialization9serializeEvRK16KVCacheEventDiffI1TERNSt7ostreamE)
    - [`deserializeKVCacheEventDiff()`](#_CPPv4I0EN12tensorrt_llm8executor13Serialization27deserializeKVCacheEventDiffE16KVCacheEventDiffI1TERNSt7istreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERK18KVCacheUpdatedData)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERK18KVCacheUpdatedDataRNSt7ostreamE)
    - [`deserializeKVCacheUpdatedData()`](#_CPPv4N12tensorrt_llm8executor13Serialization29deserializeKVCacheUpdatedDataERNSt7istreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor13Serialization14serializedSizeERKN12tensorrt_llm7runtime11UniqueTokenE)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor13Serialization9serializeERKN12tensorrt_llm7runtime11UniqueTokenERNSt7ostreamE)
    - [`deserializeUniqueToken()`](#_CPPv4N12tensorrt_llm8executor13Serialization22deserializeUniqueTokenERNSt7istreamE)
    - [`deserializeString()`](#_CPPv4N12tensorrt_llm8executor13Serialization17deserializeStringERNSt7istreamE)
    - [`deserializeBool()`](#_CPPv4N12tensorrt_llm8executor13Serialization15deserializeBoolERNSt7istreamE)
    - [`deserializeModelType()`](#_CPPv4N12tensorrt_llm8executor13Serialization20deserializeModelTypeERNSt7istreamE)
* [disaggServerUtil.h](#disaggserverutil-h)
  + [`tensorrt_llm::executor::disagg_executor`](#_CPPv4N12tensorrt_llm8executor15disagg_executorE)
    - [`tensorrt_llm::executor::disagg_executor::DisaggExecutorOrchestrator`](#_CPPv4N12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestratorE)
      * [`DisaggExecutorOrchestrator()`](#_CPPv4N12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestrator26DisaggExecutorOrchestratorERKNSt6vectorINSt10filesystem4pathEEERKNSt6vectorINSt10filesystem4pathEEERKNSt6vectorIN8executor14ExecutorConfigEEERKNSt6vectorIN8executor14ExecutorConfigEEEbb)
      * [`enqueueContext()`](#_CPPv4N12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestrator14enqueueContextERKNSt6vectorIN5texec7RequestEEENSt8optionalIiEEb)
      * [`enqueueGeneration()`](#_CPPv4N12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestrator17enqueueGenerationERKNSt6vectorIN5texec7RequestEEERKNSt6vectorI6IdTypeEENSt8optionalIiEEb)
      * [`awaitContextResponses()`](#_CPPv4N12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestrator21awaitContextResponsesERKNSt8optionalINSt6chrono12millisecondsEEENSt8optionalIiEE)
      * [`awaitGenerationResponses()`](#_CPPv4N12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestrator24awaitGenerationResponsesERKNSt8optionalINSt6chrono12millisecondsEEENSt8optionalIiEE)
      * [`canEnqueue()`](#_CPPv4NK12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestrator10canEnqueueEv)
      * [`getContextExecutors()`](#_CPPv4NK12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestrator19getContextExecutorsEv)
      * [`getGenExecutors()`](#_CPPv4NK12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestrator15getGenExecutorsEv)
      * [`~DisaggExecutorOrchestrator()`](#_CPPv4N12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestratorD0Ev)
      * [`mImpl`](#_CPPv4N12tensorrt_llm8executor15disagg_executor26DisaggExecutorOrchestrator5mImplE)
    - [`tensorrt_llm::executor::disagg_executor::ResponseWithId`](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithIdE)
      * [`ResponseWithId()`](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithId14ResponseWithIdERRN12tensorrt_llm8executor8ResponseE6IdType)
      * [`ResponseWithId()`](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithId14ResponseWithIdERKN12tensorrt_llm8executor8ResponseE6IdType)
      * [`ResponseWithId()`](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithId14ResponseWithIdERR14ResponseWithId)
      * [`ResponseWithId()`](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithId14ResponseWithIdERK14ResponseWithId)
      * [`operator=()`](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithIdaSERR14ResponseWithId)
      * [`operator=()`](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithIdaSERK14ResponseWithId)
      * [`~ResponseWithId()`](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithIdD0Ev)
      * [`response`](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithId8responseE)
      * [`gid`](#_CPPv4N12tensorrt_llm8executor15disagg_executor14ResponseWithId3gidE)
* [dataTransceiverState.h](#datatransceiverstate-h)
  + [`tensorrt_llm::executor::DataTransceiverState`](#_CPPv4N12tensorrt_llm8executor20DataTransceiverStateE)
    - [`DataTransceiverState()`](#_CPPv4N12tensorrt_llm8executor20DataTransceiverState20DataTransceiverStateEv)
    - [`DataTransceiverState()`](#_CPPv4N12tensorrt_llm8executor20DataTransceiverState20DataTransceiverStateEN8kv_cache10CacheStateEN8kv_cache9CommStateE)
    - [`setCacheState()`](#_CPPv4N12tensorrt_llm8executor20DataTransceiverState13setCacheStateEN8kv_cache10CacheStateE)
    - [`getCacheState()`](#_CPPv4NK12tensorrt_llm8executor20DataTransceiverState13getCacheStateEv)
    - [`setCommState()`](#_CPPv4N12tensorrt_llm8executor20DataTransceiverState12setCommStateEN8kv_cache9CommStateE)
    - [`getCommState()`](#_CPPv4NK12tensorrt_llm8executor20DataTransceiverState12getCommStateEv)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor20DataTransceiverStateeqERK20DataTransceiverState)
    - [`toString()`](#_CPPv4NK12tensorrt_llm8executor20DataTransceiverState8toStringEv)
    - [`mCacheState`](#_CPPv4N12tensorrt_llm8executor20DataTransceiverState11mCacheStateE)
    - [`mCommState`](#_CPPv4N12tensorrt_llm8executor20DataTransceiverState10mCommStateE)
  + [`tensorrt_llm::executor::kv_cache::AgentState`](#_CPPv4N12tensorrt_llm8executor8kv_cache10AgentStateE)
    - [`AgentState()`](#_CPPv4N12tensorrt_llm8executor8kv_cache10AgentState10AgentStateENSt6stringENSt6stringE)
    - [`AgentState()`](#_CPPv4N12tensorrt_llm8executor8kv_cache10AgentState10AgentStateEv)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache10AgentStateeqERK10AgentState)
    - [`toString()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache10AgentState8toStringEv)
    - [`mAgentName`](#_CPPv4N12tensorrt_llm8executor8kv_cache10AgentState10mAgentNameE)
    - [`mConnectionInfo`](#_CPPv4N12tensorrt_llm8executor8kv_cache10AgentState15mConnectionInfoE)
  + [`tensorrt_llm::executor::kv_cache::CacheState`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheStateE)
    - [`AttentionType`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState13AttentionTypeE)
      * [`kDEFAULT`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState13AttentionType8kDEFAULTE)
      * [`kMLA`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState13AttentionType4kMLAE)
    - [`CacheState()`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState10CacheStateE11ModelConfigRKN7runtime11WorldConfigERKNSt6vectorI10SizeType32EEN8nvinfer18DataTypeE13AttentionTypei)
    - [`CacheState()`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState10CacheStateENSt6vectorI10SizeType32EE10SizeType3210SizeType3210SizeType3210SizeType3210SizeType32RKNSt6vectorI10SizeType32EEN8nvinfer18DataTypeE13AttentionTypeibii)
    - [`CacheState()`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState10CacheStateE10SizeType3210SizeType3210SizeType3210SizeType3210SizeType3210SizeType3210SizeType32RKNSt6vectorI10SizeType32EEN8nvinfer18DataTypeE13AttentionTypeibii)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache10CacheStateeqERKN8kv_cache10CacheStateE)
    - [`getModelConfig()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache10CacheState14getModelConfigEv)
    - [`getParallelConfig()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache10CacheState17getParallelConfigEv)
    - [`getAttentionConfig()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache10CacheState18getAttentionConfigEv)
    - [`getDataType()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache10CacheState11getDataTypeEv)
    - [`toString()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache10CacheState8toStringEv)
    - [`mModelConfig`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState12mModelConfigE)
    - [`mParallelConfig`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState15mParallelConfigE)
    - [`mDataType`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState9mDataTypeE)
    - [`mAttentionConfig`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState16mAttentionConfigE)
    - [`tensorrt_llm::executor::kv_cache::CacheState::AttentionConfig`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState15AttentionConfigE)
      * [`AttentionConfig()`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState15AttentionConfig15AttentionConfigE13AttentionTypei)
      * [`operator==()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache10CacheState15AttentionConfigeqERK15AttentionConfig)
      * [`mAttentionType`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState15AttentionConfig14mAttentionTypeE)
      * [`mKvFactor`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState15AttentionConfig9mKvFactorE)
    - [`tensorrt_llm::executor::kv_cache::CacheState::ModelConfig`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState11ModelConfigE)
      * [`operator==()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache10CacheState11ModelConfigeqERK11ModelConfig)
      * [`mNbKvHeadsPerLayer`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState11ModelConfig18mNbKvHeadsPerLayerE)
      * [`mSizePerHead`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState11ModelConfig12mSizePerHeadE)
      * [`mTokensPerBlock`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState11ModelConfig15mTokensPerBlockE)
    - [`tensorrt_llm::executor::kv_cache::CacheState::ParallelConfig`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfigE)
      * [`operator==()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfigeqERK14ParallelConfig)
      * [`mTensorParallelism`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfig18mTensorParallelismE)
      * [`mPipelineParallelism`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfig20mPipelineParallelismE)
      * [`mContextParallelism`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfig19mContextParallelismE)
      * [`mEnableAttentionDP`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfig18mEnableAttentionDPE)
      * [`mDPrank`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfig7mDPrankE)
      * [`mDPsize`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfig7mDPsizeE)
      * [`mAttentionLayerNumPerPP`](#_CPPv4N12tensorrt_llm8executor8kv_cache10CacheState14ParallelConfig23mAttentionLayerNumPerPPE)
  + [`tensorrt_llm::executor::kv_cache::CommState`](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommStateE)
    - [`CommState()`](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommState9CommStateEv)
    - [`CommState()`](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommState9CommStateENSt6vectorI10SizeType32EEi)
    - [`CommState()`](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommState9CommStateENSt6vectorI11SocketStateEEi)
    - [`CommState()`](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommState9CommStateENSt8uint16_tENSt6stringE)
    - [`CommState()`](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommState9CommStateENSt6vectorI10AgentStateEEi)
    - [`isMpiState()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache9CommState10isMpiStateEv)
    - [`isSocketState()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache9CommState13isSocketStateEv)
    - [`isAgentState()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache9CommState12isAgentStateEv)
    - [`getMpiState()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache9CommState11getMpiStateEv)
    - [`getSocketState()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache9CommState14getSocketStateEv)
    - [`getAgentState()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache9CommState13getAgentStateEv)
    - [`getSelfIdx()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache9CommState10getSelfIdxEv)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache9CommStateeqERK9CommState)
    - [`toString()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache9CommState8toStringEv)
    - [`mState`](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommState6mStateE)
    - [`mSelfIdx`](#_CPPv4N12tensorrt_llm8executor8kv_cache9CommState8mSelfIdxE)
  + [`tensorrt_llm::executor::kv_cache::MpiState`](#_CPPv4N12tensorrt_llm8executor8kv_cache8MpiStateE)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache8MpiStateeqERK8MpiState)
    - [`toString()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache8MpiState8toStringEv)
    - [`mRanks`](#_CPPv4N12tensorrt_llm8executor8kv_cache8MpiState6mRanksE)
  + [`tensorrt_llm::executor::kv_cache::SocketState`](#_CPPv4N12tensorrt_llm8executor8kv_cache11SocketStateE)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache11SocketStateeqERK11SocketState)
    - [`toString()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache11SocketState8toStringEv)
    - [`mPort`](#_CPPv4N12tensorrt_llm8executor8kv_cache11SocketState5mPortE)
    - [`mIp`](#_CPPv4N12tensorrt_llm8executor8kv_cache11SocketState3mIpE)
* [tensor.h](#tensor-h)
  + [`tensorrt_llm::executor::Shape`](#_CPPv4N12tensorrt_llm8executor5ShapeE)
    - [`Base`](#_CPPv4N12tensorrt_llm8executor5Shape4BaseE)
    - [`DimType64`](#_CPPv4N12tensorrt_llm8executor5Shape9DimType64E)
    - [`Shape()`](#_CPPv4N12tensorrt_llm8executor5Shape5ShapeEv)
    - [`Shape()`](#_CPPv4N12tensorrt_llm8executor5Shape5ShapeEPK9DimType64N4Base9size_typeE)
    - [`Shape()`](#_CPPv4N12tensorrt_llm8executor5Shape5ShapeENSt16initializer_listI9DimType64EE)
  + [`tensorrt_llm::executor::Tensor`](#_CPPv4N12tensorrt_llm8executor6TensorE)
    - [`CudaStreamPtr`](#_CPPv4N12tensorrt_llm8executor6Tensor13CudaStreamPtrE)
    - [`copyToCpu()`](#_CPPv4NK12tensorrt_llm8executor6Tensor9copyToCpuEN6Tensor13CudaStreamPtrE)
    - [`copyToPinned()`](#_CPPv4NK12tensorrt_llm8executor6Tensor12copyToPinnedEN6Tensor13CudaStreamPtrE)
    - [`copyToPooledPinned()`](#_CPPv4NK12tensorrt_llm8executor6Tensor18copyToPooledPinnedEN6Tensor13CudaStreamPtrE)
    - [`copyToManaged()`](#_CPPv4NK12tensorrt_llm8executor6Tensor13copyToManagedEN6Tensor13CudaStreamPtrE)
    - [`copyToGpu()`](#_CPPv4NK12tensorrt_llm8executor6Tensor9copyToGpuEN6Tensor13CudaStreamPtrE)
    - [`Tensor()`](#_CPPv4N12tensorrt_llm8executor6Tensor6TensorEv)
    - [`~Tensor()`](#_CPPv4N12tensorrt_llm8executor6TensorD0Ev)
    - [`Tensor()`](#_CPPv4N12tensorrt_llm8executor6Tensor6TensorERK6Tensor)
    - [`Tensor()`](#_CPPv4N12tensorrt_llm8executor6Tensor6TensorERR6Tensor)
    - [`operator=()`](#_CPPv4N12tensorrt_llm8executor6TensoraSERK6Tensor)
    - [`operator=()`](#_CPPv4N12tensorrt_llm8executor6TensoraSERR6Tensor)
    - [`getData()`](#_CPPv4N12tensorrt_llm8executor6Tensor7getDataEv)
    - [`getData()`](#_CPPv4NK12tensorrt_llm8executor6Tensor7getDataEv)
    - [`getDataType()`](#_CPPv4NK12tensorrt_llm8executor6Tensor11getDataTypeEv)
    - [`getMemoryType()`](#_CPPv4NK12tensorrt_llm8executor6Tensor13getMemoryTypeEv)
    - [`getShape()`](#_CPPv4NK12tensorrt_llm8executor6Tensor8getShapeEv)
    - [`getSize()`](#_CPPv4NK12tensorrt_llm8executor6Tensor7getSizeEv)
    - [`getSizeInBytes()`](#_CPPv4NK12tensorrt_llm8executor6Tensor14getSizeInBytesEv)
    - [`setZero()`](#_CPPv4N12tensorrt_llm8executor6Tensor7setZeroE13CudaStreamPtr)
    - [`setFrom()`](#_CPPv4N12tensorrt_llm8executor6Tensor7setFromERK6Tensor13CudaStreamPtr)
    - [`operator bool()`](#_CPPv4NK12tensorrt_llm8executor6TensorcvbEv)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor6TensoreqERK6Tensor)
    - [`operator!=()`](#_CPPv4NK12tensorrt_llm8executor6TensorneERK6Tensor)
    - [`cpu()`](#_CPPv4N12tensorrt_llm8executor6Tensor3cpuE8DataType5Shape)
    - [`cpu()`](#_CPPv4I0EN12tensorrt_llm8executor6Tensor3cpuE6Tensor5Shape)
    - [`pinned()`](#_CPPv4N12tensorrt_llm8executor6Tensor6pinnedE8DataType5Shape)
    - [`pinned()`](#_CPPv4I0EN12tensorrt_llm8executor6Tensor6pinnedE6Tensor5Shape)
    - [`pooledPinned()`](#_CPPv4N12tensorrt_llm8executor6Tensor12pooledPinnedE8DataType5Shape)
    - [`pooledPinned()`](#_CPPv4I0EN12tensorrt_llm8executor6Tensor12pooledPinnedE6Tensor5Shape)
    - [`managed()`](#_CPPv4N12tensorrt_llm8executor6Tensor7managedE8DataType5Shape)
    - [`managed()`](#_CPPv4I0EN12tensorrt_llm8executor6Tensor7managedE6Tensor5Shape)
    - [`gpu()`](#_CPPv4N12tensorrt_llm8executor6Tensor3gpuE8DataType13CudaStreamPtr5Shape)
    - [`gpu()`](#_CPPv4I0EN12tensorrt_llm8executor6Tensor3gpuE6Tensor13CudaStreamPtr5Shape)
    - [`of()`](#_CPPv4N12tensorrt_llm8executor6Tensor2ofE8DataTypePv5Shape)
    - [`of()`](#_CPPv4I0EN12tensorrt_llm8executor6Tensor2ofE6TensorP1T5Shape)
    - [`of()`](#_CPPv4I0EN12tensorrt_llm8executor6Tensor2ofE6TensorR1T)
    - [`Impl`](#_CPPv4N12tensorrt_llm8executor6Tensor4ImplE)
    - [`Tensor()`](#_CPPv4N12tensorrt_llm8executor6Tensor6TensorENSt10shared_ptrIN7runtime7ITensorEEE)
    - [`copyTo()`](#_CPPv4NK12tensorrt_llm8executor6Tensor6copyToENSt10shared_ptrI4ImplEE13CudaStreamPtr)
    - [`mTensor`](#_CPPv4N12tensorrt_llm8executor6Tensor7mTensorE)
    - [`getRuntimeType()`](#_CPPv4I0EN12tensorrt_llm8executor6Tensor14getRuntimeTypeE8DataTypev)
    - [`detail::toITensor`](#_CPPv4N12tensorrt_llm8executor6Tensor6detail9toITensorERK6Tensor)
    - [`detail::ofITensor`](#_CPPv4N12tensorrt_llm8executor6Tensor6detail9ofITensorENSt10shared_ptrIN7runtime7ITensorEEE)
  + [`tensorrt_llm::executor::detail`](#_CPPv4N12tensorrt_llm8executor6detailE)
    - [`DimType64`](#_CPPv4N12tensorrt_llm8executor6detail9DimType64E)
    - [`toITensor()`](#_CPPv4N12tensorrt_llm8executor6detail9toITensorERK6Tensor)
    - [`ofITensor()`](#_CPPv4N12tensorrt_llm8executor6detail9ofITensorENSt10shared_ptrIN7runtime7ITensorEEE)
  + [`tensorrt_llm::runtime`](#_CPPv4N12tensorrt_llm7runtimeE)
* [transferAgent.h](#transferagent-h)
  + [`TransferDescs`](#_CPPv4N12tensorrt_llm8executor8kv_cache13TransferDescsE)
  + [`RegisterDescs`](#_CPPv4N12tensorrt_llm8executor8kv_cache13RegisterDescsE)
  + [`SyncMessage`](#_CPPv4N12tensorrt_llm8executor8kv_cache11SyncMessageE)
  + [`ConnectionInfoType`](#_CPPv4N12tensorrt_llm8executor8kv_cache18ConnectionInfoTypeE)
  + [`MemoryType`](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryTypeE)
    - [`kDRAM`](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryType5kDRAME)
    - [`kVRAM`](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryType5kVRAME)
    - [`kBLK`](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryType4kBLKE)
    - [`kOBJ`](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryType4kOBJE)
    - [`kFILE`](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryType5kFILEE)
  + [`TransferOp`](#_CPPv4N12tensorrt_llm8executor8kv_cache10TransferOpE)
    - [`kREAD`](#_CPPv4N12tensorrt_llm8executor8kv_cache10TransferOp5kREADE)
    - [`kWRITE`](#_CPPv4N12tensorrt_llm8executor8kv_cache10TransferOp6kWRITEE)
  + [`makeTransferAgent()`](#_CPPv4IDpEN12tensorrt_llm8executor8kv_cache17makeTransferAgentENSt10unique_ptrI17BaseTransferAgentEERKNSt6stringEDpRR4Args)
  + [`makeLoopbackAgent()`](#_CPPv4IDpEN12tensorrt_llm8executor8kv_cache17makeLoopbackAgentENSt10shared_ptrI17BaseLoopbackAgentEERKNSt6stringEDpRR4Args)
  + [`tensorrt_llm::executor::kv_cache::AgentDesc`](#_CPPv4N12tensorrt_llm8executor8kv_cache9AgentDescE)
    - [`AgentDesc()`](#_CPPv4N12tensorrt_llm8executor8kv_cache9AgentDesc9AgentDescENSt6stringE)
    - [`getBackendAgentDesc()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache9AgentDesc19getBackendAgentDescEv)
    - [`mBackendAgentDesc`](#_CPPv4N12tensorrt_llm8executor8kv_cache9AgentDesc17mBackendAgentDescE)
  + [`tensorrt_llm::executor::kv_cache::BaseAgentConfig`](#_CPPv4N12tensorrt_llm8executor8kv_cache15BaseAgentConfigE)
    - [`mName`](#_CPPv4N12tensorrt_llm8executor8kv_cache15BaseAgentConfig5mNameE)
    - [`useProgThread`](#_CPPv4N12tensorrt_llm8executor8kv_cache15BaseAgentConfig13useProgThreadE)
    - [`multiThread`](#_CPPv4N12tensorrt_llm8executor8kv_cache15BaseAgentConfig11multiThreadE)
  + [`tensorrt_llm::executor::kv_cache::BaseLoopbackAgent`](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseLoopbackAgentE)
    - [`~BaseLoopbackAgent()`](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseLoopbackAgentD0Ev)
    - [`executeLoopbackRequest()`](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseLoopbackAgent22executeLoopbackRequestERK11MemoryDescsRK9FileDescsb)
  + [`tensorrt_llm::executor::kv_cache::BaseTransferAgent`](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgentE)
    - [`~BaseTransferAgent()`](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgentD0Ev)
    - [`registerMemory()`](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent14registerMemoryERK13RegisterDescs)
    - [`deregisterMemory()`](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent16deregisterMemoryERK13RegisterDescs)
    - [`loadRemoteAgent()`](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent15loadRemoteAgentERKNSt6stringERK9AgentDesc)
    - [`getLocalAgentDesc()`](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent17getLocalAgentDescEv)
    - [`invalidateRemoteAgent()`](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent21invalidateRemoteAgentERKNSt6stringE)
    - [`submitTransferRequests()`](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent22submitTransferRequestsERK15TransferRequest)
    - [`notifySyncMessage()`](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent17notifySyncMessageERKNSt6stringERK11SyncMessage)
    - [`getNotifiedSyncMessages()`](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent23getNotifiedSyncMessagesEv)
    - [`getConnectionInfo()`](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent17getConnectionInfoEv)
    - [`connectRemoteAgent()`](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent18connectRemoteAgentERKNSt6stringERK18ConnectionInfoType)
    - [`checkRemoteDescs()`](#_CPPv4N12tensorrt_llm8executor8kv_cache17BaseTransferAgent16checkRemoteDescsERKNSt6stringERK11MemoryDescs)
  + [`tensorrt_llm::executor::kv_cache::DynLibLoader`](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoaderE)
    - [`getHandle()`](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoader9getHandleERKNSt6stringE)
    - [`getFunctionPointer()`](#_CPPv4I0EN12tensorrt_llm8executor8kv_cache12DynLibLoader18getFunctionPointerE9FunctionTRKNSt6stringERKNSt6stringE)
    - [`~DynLibLoader()`](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoaderD0Ev)
    - [`DynLibLoader()`](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoader12DynLibLoaderEv)
    - [`DynLibLoader()`](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoader12DynLibLoaderERK12DynLibLoader)
    - [`operator=()`](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoaderaSERK12DynLibLoader)
    - [`getInstance()`](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoader11getInstanceEv)
    - [`mDllMutex`](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoader9mDllMutexE)
    - [`mHandlers`](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoader9mHandlersE)
    - [`dlSym()`](#_CPPv4N12tensorrt_llm8executor8kv_cache12DynLibLoader5dlSymEPvPKc)
  + [`tensorrt_llm::executor::kv_cache::FileDesc`](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDescE)
    - [`FileDesc()`](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDesc8FileDescERKNSt6stringEi6mode_t6size_t)
    - [`FileDesc()`](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDesc8FileDescERR8FileDesc)
    - [`operator=()`](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDescaSERR8FileDesc)
    - [`~FileDesc()`](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDescD0Ev)
    - [`getFd()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache8FileDesc5getFdEv)
    - [`getLen()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache8FileDesc6getLenEv)
    - [`FileDesc()`](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDesc8FileDescERK8FileDesc)
    - [`operator=()`](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDescaSERK8FileDesc)
    - [`fd`](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDesc2fdE)
    - [`mLen`](#_CPPv4N12tensorrt_llm8executor8kv_cache8FileDesc4mLenE)
  + [`tensorrt_llm::executor::kv_cache::FileDescs`](#_CPPv4N12tensorrt_llm8executor8kv_cache9FileDescsE)
    - [`FileDescs()`](#_CPPv4N12tensorrt_llm8executor8kv_cache9FileDescs9FileDescsERRNSt6vectorI8FileDescEE)
    - [`getDescs()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache9FileDescs8getDescsEv)
    - [`mDescs`](#_CPPv4N12tensorrt_llm8executor8kv_cache9FileDescs6mDescsE)
  + [`tensorrt_llm::executor::kv_cache::MemoryDesc`](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDescE)
    - [`MemoryDesc()`](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDesc10MemoryDescERKNSt6vectorIcEE8uint32_t)
    - [`MemoryDesc()`](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDesc10MemoryDescEPv6size_t8uint32_t)
    - [`MemoryDesc()`](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDesc10MemoryDescE9uintptr_t6size_t8uint32_t)
    - [`getAddr()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache10MemoryDesc7getAddrEv)
    - [`getLen()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache10MemoryDesc6getLenEv)
    - [`getDeviceId()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache10MemoryDesc11getDeviceIdEv)
    - [`serialize()`](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDesc9serializeERK10MemoryDescRNSt7ostreamE)
    - [`deserialize()`](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDesc11deserializeERNSt7istreamE)
    - [`serializedSize()`](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDesc14serializedSizeERK10MemoryDesc)
    - [`mAddr`](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDesc5mAddrE)
    - [`mLen`](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDesc4mLenE)
    - [`mDeviceId`](#_CPPv4N12tensorrt_llm8executor8kv_cache10MemoryDesc9mDeviceIdE)
  + [`tensorrt_llm::executor::kv_cache::MemoryDescs`](#_CPPv4N12tensorrt_llm8executor8kv_cache11MemoryDescsE)
    - [`MemoryDescs()`](#_CPPv4N12tensorrt_llm8executor8kv_cache11MemoryDescs11MemoryDescsE10MemoryTypeNSt6vectorI10MemoryDescEE)
    - [`getType()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache11MemoryDescs7getTypeEv)
    - [`getDescs()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache11MemoryDescs8getDescsEv)
    - [`mType`](#_CPPv4N12tensorrt_llm8executor8kv_cache11MemoryDescs5mTypeE)
    - [`mDescs`](#_CPPv4N12tensorrt_llm8executor8kv_cache11MemoryDescs6mDescsE)
  + [`tensorrt_llm::executor::kv_cache::TransferRequest`](#_CPPv4N12tensorrt_llm8executor8kv_cache15TransferRequestE)
    - [`TransferRequest()`](#_CPPv4N12tensorrt_llm8executor8kv_cache15TransferRequest15TransferRequestE10TransferOp13TransferDescs13TransferDescsRKNSt6stringENSt8optionalI11SyncMessageEE)
    - [`getOp()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache15TransferRequest5getOpEv)
    - [`getSrcDescs()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache15TransferRequest11getSrcDescsEv)
    - [`getDstDescs()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache15TransferRequest11getDstDescsEv)
    - [`getRemoteName()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache15TransferRequest13getRemoteNameEv)
    - [`getSyncMessage()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache15TransferRequest14getSyncMessageEv)
    - [`mOp`](#_CPPv4N12tensorrt_llm8executor8kv_cache15TransferRequest3mOpE)
    - [`mSrcDescs`](#_CPPv4N12tensorrt_llm8executor8kv_cache15TransferRequest9mSrcDescsE)
    - [`mDstDescs`](#_CPPv4N12tensorrt_llm8executor8kv_cache15TransferRequest9mDstDescsE)
    - [`mRemoteName`](#_CPPv4N12tensorrt_llm8executor8kv_cache15TransferRequest11mRemoteNameE)
    - [`mSyncMessage`](#_CPPv4N12tensorrt_llm8executor8kv_cache15TransferRequest12mSyncMessageE)
  + [`tensorrt_llm::executor::kv_cache::TransferStatus`](#_CPPv4N12tensorrt_llm8executor8kv_cache14TransferStatusE)
    - [`~TransferStatus()`](#_CPPv4N12tensorrt_llm8executor8kv_cache14TransferStatusD0Ev)
    - [`isCompleted()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache14TransferStatus11isCompletedEv)
    - [`wait()`](#_CPPv4NK12tensorrt_llm8executor8kv_cache14TransferStatus4waitEv)
* [executor.h](#executor-h)
  + [`tensorrt_llm::batch_manager`](#_CPPv4N12tensorrt_llm13batch_managerE)
    - [`tensorrt_llm::batch_manager::kv_cache_manager`](#_CPPv4N12tensorrt_llm13batch_manager16kv_cache_managerE)
  + [`RetentionPriority`](#_CPPv4N12tensorrt_llm8executor17RetentionPriorityE)
  + [`KVCacheEventData`](#_CPPv4N12tensorrt_llm8executor16KVCacheEventDataE)
  + [`version()`](#_CPPv4N12tensorrt_llm8executor7versionEv)
  + [`tensorrt_llm::executor::AdditionalModelOutput`](#_CPPv4N12tensorrt_llm8executor21AdditionalModelOutputE)
    - [`AdditionalModelOutput()`](#_CPPv4N12tensorrt_llm8executor21AdditionalModelOutput21AdditionalModelOutputENSt6stringEb)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor21AdditionalModelOutputeqERK21AdditionalModelOutput)
    - [`name`](#_CPPv4N12tensorrt_llm8executor21AdditionalModelOutput4nameE)
    - [`gatherContext`](#_CPPv4N12tensorrt_llm8executor21AdditionalModelOutput13gatherContextE)
  + [`tensorrt_llm::executor::AdditionalOutput`](#_CPPv4N12tensorrt_llm8executor16AdditionalOutputE)
    - [`AdditionalOutput()`](#_CPPv4N12tensorrt_llm8executor16AdditionalOutput16AdditionalOutputENSt6stringE6Tensor)
    - [`AdditionalOutput()`](#_CPPv4N12tensorrt_llm8executor16AdditionalOutput16AdditionalOutputERK16AdditionalOutput)
    - [`AdditionalOutput()`](#_CPPv4N12tensorrt_llm8executor16AdditionalOutput16AdditionalOutputERR16AdditionalOutput)
    - [`operator=()`](#_CPPv4N12tensorrt_llm8executor16AdditionalOutputaSERK16AdditionalOutput)
    - [`operator=()`](#_CPPv4N12tensorrt_llm8executor16AdditionalOutputaSERR16AdditionalOutput)
    - [`~AdditionalOutput()`](#_CPPv4N12tensorrt_llm8executor16AdditionalOutputD0Ev)
    - [`name`](#_CPPv4N12tensorrt_llm8executor16AdditionalOutput4nameE)
    - [`output`](#_CPPv4N12tensorrt_llm8executor16AdditionalOutput6outputE)
  + [`tensorrt_llm::executor::CacheTransceiverConfig`](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfigE)
    - [`BackendType`](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig11BackendTypeE)
      * [`DEFAULT`](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig11BackendType7DEFAULTE)
      * [`MPI`](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig11BackendType3MPIE)
      * [`UCX`](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig11BackendType3UCXE)
      * [`NIXL`](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig11BackendType4NIXLE)
    - [`CacheTransceiverConfig()`](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig22CacheTransceiverConfigENSt8optionalI11BackendTypeEENSt8optionalI6size_tEE)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor22CacheTransceiverConfigeqERK22CacheTransceiverConfig)
    - [`setBackendType()`](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig14setBackendTypeENSt8optionalI11BackendTypeEE)
    - [`setMaxTokensInBuffer()`](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig20setMaxTokensInBufferENSt8optionalI6size_tEE)
    - [`getMaxTokensInBuffer()`](#_CPPv4NK12tensorrt_llm8executor22CacheTransceiverConfig20getMaxTokensInBufferEv)
    - [`getBackendType()`](#_CPPv4NK12tensorrt_llm8executor22CacheTransceiverConfig14getBackendTypeEv)
    - [`mBackendType`](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig12mBackendTypeE)
    - [`mMaxTokensInBuffer`](#_CPPv4N12tensorrt_llm8executor22CacheTransceiverConfig18mMaxTokensInBufferE)
  + [`tensorrt_llm::executor::ContextPhaseParams`](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsE)
    - [`RequestIdType`](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams13RequestIdTypeE)
    - [`ContextPhaseParams()`](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams18ContextPhaseParamsE9VecTokens13RequestIdTypeNSt8optionalI9VecTokensEE)
    - [`ContextPhaseParams()`](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams18ContextPhaseParamsE9VecTokens13RequestIdTypePvNSt8optionalI9VecTokensEE)
    - [`ContextPhaseParams()`](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams18ContextPhaseParamsE9VecTokens13RequestIdTypeRKNSt6vectorIcEENSt8optionalI9VecTokensEE)
    - [`ContextPhaseParams()`](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams18ContextPhaseParamsERK18ContextPhaseParams)
    - [`ContextPhaseParams()`](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams18ContextPhaseParamsERR18ContextPhaseParams)
    - [`operator=()`](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsaSERK18ContextPhaseParams)
    - [`operator=()`](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsaSERR18ContextPhaseParams)
    - [`~ContextPhaseParams()`](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParamsD0Ev)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor18ContextPhaseParamseqERK18ContextPhaseParams)
    - [`getFirstGenTokens()`](#_CPPv4NKR12tensorrt_llm8executor18ContextPhaseParams17getFirstGenTokensEv)
    - [`getDraftTokens()`](#_CPPv4NKR12tensorrt_llm8executor18ContextPhaseParams14getDraftTokensEv)
    - [`popFirstGenTokens()`](#_CPPv4NO12tensorrt_llm8executor18ContextPhaseParams17popFirstGenTokensEv)
    - [`getReqId()`](#_CPPv4NK12tensorrt_llm8executor18ContextPhaseParams8getReqIdEv)
    - [`getState()`](#_CPPv4NK12tensorrt_llm8executor18ContextPhaseParams8getStateEv)
    - [`getState()`](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams8getStateEv)
    - [`releaseState()`](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams12releaseStateEv)
    - [`getSerializedState()`](#_CPPv4NK12tensorrt_llm8executor18ContextPhaseParams18getSerializedStateEv)
    - [`StatePtr`](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams8StatePtrE)
    - [`mReqId`](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams6mReqIdE)
    - [`mFirstGenTokens`](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams15mFirstGenTokensE)
    - [`mState`](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams6mStateE)
    - [`mDraftTokens`](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams12mDraftTokensE)
    - [`deleter()`](#_CPPv4N12tensorrt_llm8executor18ContextPhaseParams7deleterEPKv)
  + [`tensorrt_llm::executor::DebugConfig`](#_CPPv4N12tensorrt_llm8executor11DebugConfigE)
    - [`DebugConfig()`](#_CPPv4N12tensorrt_llm8executor11DebugConfig11DebugConfigEbb9StringVec10SizeType32)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor11DebugConfigeqERK11DebugConfig)
    - [`getDebugInputTensors()`](#_CPPv4NK12tensorrt_llm8executor11DebugConfig20getDebugInputTensorsEv)
    - [`getDebugOutputTensors()`](#_CPPv4NK12tensorrt_llm8executor11DebugConfig21getDebugOutputTensorsEv)
    - [`getDebugTensorNames()`](#_CPPv4NK12tensorrt_llm8executor11DebugConfig19getDebugTensorNamesEv)
    - [`getDebugTensorsMaxIterations()`](#_CPPv4NK12tensorrt_llm8executor11DebugConfig28getDebugTensorsMaxIterationsEv)
    - [`setDebugInputTensors()`](#_CPPv4N12tensorrt_llm8executor11DebugConfig20setDebugInputTensorsEb)
    - [`setDebugOutputTensors()`](#_CPPv4N12tensorrt_llm8executor11DebugConfig21setDebugOutputTensorsEb)
    - [`setDebugTensorNames()`](#_CPPv4N12tensorrt_llm8executor11DebugConfig19setDebugTensorNamesERK9StringVec)
    - [`setDebugTensorsMaxIterations()`](#_CPPv4N12tensorrt_llm8executor11DebugConfig28setDebugTensorsMaxIterationsE10SizeType32)
    - [`StringVec`](#_CPPv4N12tensorrt_llm8executor11DebugConfig9StringVecE)
    - [`mDebugInputTensors`](#_CPPv4N12tensorrt_llm8executor11DebugConfig18mDebugInputTensorsE)
    - [`mDebugOutputTensors`](#_CPPv4N12tensorrt_llm8executor11DebugConfig19mDebugOutputTensorsE)
    - [`mDebugTensorNames`](#_CPPv4N12tensorrt_llm8executor11DebugConfig17mDebugTensorNamesE)
    - [`mDebugTensorsMaxIterations`](#_CPPv4N12tensorrt_llm8executor11DebugConfig26mDebugTensorsMaxIterationsE)
  + [`tensorrt_llm::executor::DecodingConfig`](#_CPPv4N12tensorrt_llm8executor14DecodingConfigE)
    - [`DecodingConfig()`](#_CPPv4N12tensorrt_llm8executor14DecodingConfig14DecodingConfigENSt8optionalI12DecodingModeEENSt8optionalI23LookaheadDecodingConfigEENSt8optionalI13MedusaChoicesEENSt8optionalI11EagleConfigEE)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor14DecodingConfigeqERK14DecodingConfig)
    - [`setDecodingMode()`](#_CPPv4N12tensorrt_llm8executor14DecodingConfig15setDecodingModeERK12DecodingMode)
    - [`getDecodingMode()`](#_CPPv4NK12tensorrt_llm8executor14DecodingConfig15getDecodingModeEv)
    - [`setLookaheadDecodingConfig()`](#_CPPv4N12tensorrt_llm8executor14DecodingConfig26setLookaheadDecodingConfigERK23LookaheadDecodingConfig)
    - [`enableSeamlessLookaheadDecoding()`](#_CPPv4N12tensorrt_llm8executor14DecodingConfig31enableSeamlessLookaheadDecodingEv)
    - [`getLookaheadDecodingConfig()`](#_CPPv4NK12tensorrt_llm8executor14DecodingConfig26getLookaheadDecodingConfigEv)
    - [`getLookaheadDecodingMaxNumRequest()`](#_CPPv4NK12tensorrt_llm8executor14DecodingConfig33getLookaheadDecodingMaxNumRequestEv)
    - [`setMedusaChoices()`](#_CPPv4N12tensorrt_llm8executor14DecodingConfig16setMedusaChoicesERK13MedusaChoices)
    - [`getMedusaChoices()`](#_CPPv4NK12tensorrt_llm8executor14DecodingConfig16getMedusaChoicesEv)
    - [`setEagleConfig()`](#_CPPv4N12tensorrt_llm8executor14DecodingConfig14setEagleConfigERK11EagleConfig)
    - [`getEagleConfig()`](#_CPPv4NK12tensorrt_llm8executor14DecodingConfig14getEagleConfigEv)
    - [`mDecodingMode`](#_CPPv4N12tensorrt_llm8executor14DecodingConfig13mDecodingModeE)
    - [`mLookaheadDecodingConfig`](#_CPPv4N12tensorrt_llm8executor14DecodingConfig24mLookaheadDecodingConfigE)
    - [`mMedusaChoices`](#_CPPv4N12tensorrt_llm8executor14DecodingConfig14mMedusaChoicesE)
    - [`mEagleConfig`](#_CPPv4N12tensorrt_llm8executor14DecodingConfig12mEagleConfigE)
    - [`mLookaheadDecodingMaxNumRequest`](#_CPPv4N12tensorrt_llm8executor14DecodingConfig31mLookaheadDecodingMaxNumRequestE)
  + [`tensorrt_llm::executor::DynamicBatchConfig`](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfigE)
    - [`DynamicBatchConfig()`](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfig18DynamicBatchConfigEbb10SizeType32NSt6vectorINSt4pairI10SizeType3210SizeType32EEEE)
    - [`getDynamicBatchMovingAverageWindow()`](#_CPPv4NK12tensorrt_llm8executor18DynamicBatchConfig34getDynamicBatchMovingAverageWindowEv)
    - [`getEnableBatchSizeTuning()`](#_CPPv4NK12tensorrt_llm8executor18DynamicBatchConfig24getEnableBatchSizeTuningEv)
    - [`getEnableMaxNumTokensTuning()`](#_CPPv4NK12tensorrt_llm8executor18DynamicBatchConfig27getEnableMaxNumTokensTuningEv)
    - [`getBatchSizeTable()`](#_CPPv4NK12tensorrt_llm8executor18DynamicBatchConfig17getBatchSizeTableEv)
    - [`kDefaultDynamicBatchMovingAverageWindow`](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfig39kDefaultDynamicBatchMovingAverageWindowE)
    - [`kDefaultBatchSizeTable`](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfig22kDefaultBatchSizeTableE)
    - [`mEnableBatchSizeTuning`](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfig22mEnableBatchSizeTuningE)
    - [`mEnableMaxNumTokensTuning`](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfig25mEnableMaxNumTokensTuningE)
    - [`mDynamicBatchMovingAverageWindow`](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfig32mDynamicBatchMovingAverageWindowE)
    - [`mBatchSizeTable`](#_CPPv4N12tensorrt_llm8executor18DynamicBatchConfig15mBatchSizeTableE)
  + [`tensorrt_llm::executor::EagleConfig`](#_CPPv4N12tensorrt_llm8executor11EagleConfigE)
    - [`EagleConfig()`](#_CPPv4N12tensorrt_llm8executor11EagleConfig11EagleConfigENSt8optionalI12EagleChoicesEEbNSt8optionalIfEEbNSt8optionalI10SizeType32EE)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor11EagleConfigeqERK11EagleConfig)
    - [`getEagleChoices()`](#_CPPv4NK12tensorrt_llm8executor11EagleConfig15getEagleChoicesEv)
    - [`getPosteriorThreshold()`](#_CPPv4NK12tensorrt_llm8executor11EagleConfig21getPosteriorThresholdEv)
    - [`isGreedySampling()`](#_CPPv4NK12tensorrt_llm8executor11EagleConfig16isGreedySamplingEv)
    - [`useDynamicTree()`](#_CPPv4NK12tensorrt_llm8executor11EagleConfig14useDynamicTreeEv)
    - [`getDynamicTreeMaxTopK()`](#_CPPv4NK12tensorrt_llm8executor11EagleConfig21getDynamicTreeMaxTopKEv)
    - [`checkPosteriorValue()`](#_CPPv4N12tensorrt_llm8executor11EagleConfig19checkPosteriorValueERKNSt8optionalIfEE)
    - [`mEagleChoices`](#_CPPv4N12tensorrt_llm8executor11EagleConfig13mEagleChoicesE)
    - [`mGreedySampling`](#_CPPv4N12tensorrt_llm8executor11EagleConfig15mGreedySamplingE)
    - [`mPosteriorThreshold`](#_CPPv4N12tensorrt_llm8executor11EagleConfig19mPosteriorThresholdE)
    - [`mUseDynamicTree`](#_CPPv4N12tensorrt_llm8executor11EagleConfig15mUseDynamicTreeE)
    - [`mDynamicTreeMaxTopK`](#_CPPv4N12tensorrt_llm8executor11EagleConfig19mDynamicTreeMaxTopKE)
  + [`tensorrt_llm::executor::Executor`](#_CPPv4N12tensorrt_llm8executor8ExecutorE)
    - [`Executor()`](#_CPPv4N12tensorrt_llm8executor8Executor8ExecutorERKNSt10filesystem4pathE9ModelTypeRK14ExecutorConfig)
    - [`Executor()`](#_CPPv4N12tensorrt_llm8executor8Executor8ExecutorERKNSt10filesystem4pathERKNSt10filesystem4pathE9ModelTypeRK14ExecutorConfig)
    - [`Executor()`](#_CPPv4N12tensorrt_llm8executor8Executor8ExecutorERK10BufferViewRKNSt6stringE9ModelTypeRK14ExecutorConfigRKNSt8optionalINSt3mapINSt6stringE6TensorEEEE)
    - [`Executor()`](#_CPPv4N12tensorrt_llm8executor8Executor8ExecutorERK10BufferViewRKNSt6stringERK10BufferViewRKNSt6stringE9ModelTypeRK14ExecutorConfig)
    - [`Executor()`](#_CPPv4N12tensorrt_llm8executor8Executor8ExecutorENSt10shared_ptrI5ModelEERK14ExecutorConfig)
    - [`Executor()`](#_CPPv4N12tensorrt_llm8executor8Executor8ExecutorENSt10shared_ptrI5ModelEENSt10shared_ptrI5ModelEERK14ExecutorConfig)
    - [`~Executor()`](#_CPPv4N12tensorrt_llm8executor8ExecutorD0Ev)
    - [`Executor()`](#_CPPv4N12tensorrt_llm8executor8Executor8ExecutorERK8Executor)
    - [`operator=()`](#_CPPv4N12tensorrt_llm8executor8ExecutoraSERK8Executor)
    - [`Executor()`](#_CPPv4N12tensorrt_llm8executor8Executor8ExecutorERR8Executor)
    - [`operator=()`](#_CPPv4N12tensorrt_llm8executor8ExecutoraSERR8Executor)
    - [`enqueueRequest()`](#_CPPv4N12tensorrt_llm8executor8Executor14enqueueRequestERK7Request)
    - [`enqueueRequests()`](#_CPPv4N12tensorrt_llm8executor8Executor15enqueueRequestsERKNSt6vectorI7RequestEE)
    - [`awaitResponses()`](#_CPPv4N12tensorrt_llm8executor8Executor14awaitResponsesERKNSt8optionalINSt6chrono12millisecondsEEE)
    - [`awaitResponses()`](#_CPPv4N12tensorrt_llm8executor8Executor14awaitResponsesERK6IdTypeRKNSt8optionalINSt6chrono12millisecondsEEE)
    - [`awaitResponses()`](#_CPPv4N12tensorrt_llm8executor8Executor14awaitResponsesERKNSt6vectorI6IdTypeEERKNSt8optionalINSt6chrono12millisecondsEEE)
    - [`getNumResponsesReady()`](#_CPPv4NK12tensorrt_llm8executor8Executor20getNumResponsesReadyERKNSt8optionalI6IdTypeEE)
    - [`cancelRequest()`](#_CPPv4N12tensorrt_llm8executor8Executor13cancelRequestE6IdType)
    - [`shutdown()`](#_CPPv4N12tensorrt_llm8executor8Executor8shutdownEv)
    - [`getLatestIterationStats()`](#_CPPv4N12tensorrt_llm8executor8Executor23getLatestIterationStatsEv)
    - [`getLatestRequestStats()`](#_CPPv4N12tensorrt_llm8executor8Executor21getLatestRequestStatsEv)
    - [`getLatestDebugTensors()`](#_CPPv4N12tensorrt_llm8executor8Executor21getLatestDebugTensorsEv)
    - [`canEnqueueRequests()`](#_CPPv4NK12tensorrt_llm8executor8Executor18canEnqueueRequestsEv)
    - [`isParticipant()`](#_CPPv4NK12tensorrt_llm8executor8Executor13isParticipantEv)
    - [`getKVCacheEventManager()`](#_CPPv4NK12tensorrt_llm8executor8Executor22getKVCacheEventManagerEv)
    - [`mImpl`](#_CPPv4N12tensorrt_llm8executor8Executor5mImplE)
  + [`tensorrt_llm::executor::ExecutorConfig`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfigE)
    - [`ExecutorConfig()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig14ExecutorConfigE10SizeType3215SchedulerConfig13KvCacheConfigbb10SizeType3210SizeType3212BatchingTypeNSt8optionalI10SizeType32EENSt8optionalI10SizeType32EENSt8optionalI14ParallelConfigEERKNSt8optionalI15PeftCacheConfigEENSt8optionalI25LogitsPostProcessorConfigEENSt8optionalI14DecodingConfigEEbfNSt8optionalI10SizeType32EERK29ExtendedRuntimePerfKnobConfigNSt8optionalI11DebugConfigEE10SizeType328uint64_tNSt8optionalI25SpeculativeDecodingConfigEENSt8optionalI20GuidedDecodingConfigEENSt8optionalINSt6vectorI21AdditionalModelOutputEEEENSt8optionalI22CacheTransceiverConfigEEbbbb)
    - [`getMaxBeamWidth()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig15getMaxBeamWidthEv)
    - [`getSchedulerConfig()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig18getSchedulerConfigEv)
    - [`getKvCacheConfig()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig16getKvCacheConfigEv)
    - [`getSchedulerConfigRef()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig21getSchedulerConfigRefEv)
    - [`getKvCacheConfigRef()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig19getKvCacheConfigRefEv)
    - [`getEnableChunkedContext()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig23getEnableChunkedContextEv)
    - [`getNormalizeLogProbs()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig20getNormalizeLogProbsEv)
    - [`getIterStatsMaxIterations()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig25getIterStatsMaxIterationsEv)
    - [`getRequestStatsMaxIterations()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig28getRequestStatsMaxIterationsEv)
    - [`getBatchingType()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig15getBatchingTypeEv)
    - [`getMaxBatchSize()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig15getMaxBatchSizeEv)
    - [`getMaxNumTokens()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig15getMaxNumTokensEv)
    - [`getParallelConfig()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig17getParallelConfigEv)
    - [`getPeftCacheConfig()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig18getPeftCacheConfigEv)
    - [`getLogitsPostProcessorConfig()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig28getLogitsPostProcessorConfigEv)
    - [`getDecodingConfig()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig17getDecodingConfigEv)
    - [`getUseGpuDirectStorage()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig22getUseGpuDirectStorageEv)
    - [`getGpuWeightsPercent()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig20getGpuWeightsPercentEv)
    - [`getMaxQueueSize()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig15getMaxQueueSizeEv)
    - [`getExtendedRuntimePerfKnobConfig()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig32getExtendedRuntimePerfKnobConfigEv)
    - [`getDebugConfig()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig14getDebugConfigEv)
    - [`getRecvPollPeriodMs()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig19getRecvPollPeriodMsEv)
    - [`getMaxSeqIdleMicroseconds()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig25getMaxSeqIdleMicrosecondsEv)
    - [`getSpecDecConfig()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig16getSpecDecConfigEv)
    - [`getGuidedDecodingConfig()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig23getGuidedDecodingConfigEv)
    - [`getAdditionalModelOutputs()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig25getAdditionalModelOutputsEv)
    - [`getGatherGenerationLogits()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig25getGatherGenerationLogitsEv)
    - [`getPromptTableOffloading()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig24getPromptTableOffloadingEv)
    - [`getCacheTransceiverConfig()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig25getCacheTransceiverConfigEv)
    - [`getEnableTrtOverlap()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig19getEnableTrtOverlapEv)
    - [`getFailFastOnAttentionWindowTooLarge()`](#_CPPv4NK12tensorrt_llm8executor14ExecutorConfig36getFailFastOnAttentionWindowTooLargeEv)
    - [`setMaxBeamWidth()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig15setMaxBeamWidthE10SizeType32)
    - [`setMaxBatchSize()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig15setMaxBatchSizeE10SizeType32)
    - [`setMaxNumTokens()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig15setMaxNumTokensE10SizeType32)
    - [`setSchedulerConfig()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig18setSchedulerConfigERK15SchedulerConfig)
    - [`setKvCacheConfig()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig16setKvCacheConfigERK13KvCacheConfig)
    - [`setEnableChunkedContext()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig23setEnableChunkedContextEb)
    - [`setNormalizeLogProbs()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig20setNormalizeLogProbsEb)
    - [`setIterStatsMaxIterations()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig25setIterStatsMaxIterationsE10SizeType32)
    - [`setRequestStatsMaxIterations()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig28setRequestStatsMaxIterationsE10SizeType32)
    - [`setBatchingType()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig15setBatchingTypeE12BatchingType)
    - [`setParallelConfig()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig17setParallelConfigERK14ParallelConfig)
    - [`setPeftCacheConfig()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig18setPeftCacheConfigERK15PeftCacheConfig)
    - [`setLogitsPostProcessorConfig()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig28setLogitsPostProcessorConfigERK25LogitsPostProcessorConfig)
    - [`setDecodingConfig()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig17setDecodingConfigERK14DecodingConfig)
    - [`setUseGpuDirectStorage()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig22setUseGpuDirectStorageERKb)
    - [`setGpuWeightsPercent()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig20setGpuWeightsPercentERKf)
    - [`setMaxQueueSize()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig15setMaxQueueSizeERKNSt8optionalI10SizeType32EE)
    - [`setExtendedRuntimePerfKnobConfig()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig32setExtendedRuntimePerfKnobConfigERK29ExtendedRuntimePerfKnobConfig)
    - [`setDebugConfig()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig14setDebugConfigERK11DebugConfig)
    - [`setRecvPollPeriodMs()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig19setRecvPollPeriodMsERK10SizeType32)
    - [`setMaxSeqIdleMicroseconds()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig25setMaxSeqIdleMicrosecondsE8uint64_t)
    - [`setSpecDecConfig()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig16setSpecDecConfigERK25SpeculativeDecodingConfig)
    - [`setGuidedDecodingConfig()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig23setGuidedDecodingConfigERK20GuidedDecodingConfig)
    - [`setAdditionalModelOutputs()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig25setAdditionalModelOutputsERKNSt6vectorI21AdditionalModelOutputEE)
    - [`setGatherGenerationLogits()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig25setGatherGenerationLogitsEb)
    - [`setPromptTableOffloading()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig24setPromptTableOffloadingEb)
    - [`setCacheTransceiverConfig()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig25setCacheTransceiverConfigERK22CacheTransceiverConfig)
    - [`setEnableTrtOverlap()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig19setEnableTrtOverlapEb)
    - [`setFailFastOnAttentionWindowTooLarge()`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig36setFailFastOnAttentionWindowTooLargeEb)
    - [`kDefaultMaxSeqIdleMicroseconds`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig30kDefaultMaxSeqIdleMicrosecondsE)
    - [`kDefaultIterStatsMaxIterations`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig30kDefaultIterStatsMaxIterationsE)
    - [`kDefaultRequestStatsMaxIterations`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig33kDefaultRequestStatsMaxIterationsE)
    - [`mMaxBeamWidth`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig13mMaxBeamWidthE)
    - [`mSchedulerConfig`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig16mSchedulerConfigE)
    - [`mKvCacheConfig`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig14mKvCacheConfigE)
    - [`mEnableChunkedContext`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig21mEnableChunkedContextE)
    - [`mNormalizeLogProbs`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig18mNormalizeLogProbsE)
    - [`mIterStatsMaxIterations`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig23mIterStatsMaxIterationsE)
    - [`mRequestStatsMaxIterations`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig26mRequestStatsMaxIterationsE)
    - [`mBatchingType`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig13mBatchingTypeE)
    - [`mMaxBatchSize`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig13mMaxBatchSizeE)
    - [`mMaxNumTokens`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig13mMaxNumTokensE)
    - [`mParallelConfig`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig15mParallelConfigE)
    - [`mPeftCacheConfig`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig16mPeftCacheConfigE)
    - [`mLogitsPostProcessorConfig`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig26mLogitsPostProcessorConfigE)
    - [`mDecodingConfig`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig15mDecodingConfigE)
    - [`mUseGpuDirectStorage`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig20mUseGpuDirectStorageE)
    - [`mGpuWeightsPercent`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig18mGpuWeightsPercentE)
    - [`mMaxQueueSize`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig13mMaxQueueSizeE)
    - [`mExtendedRuntimePerfKnobConfig`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig30mExtendedRuntimePerfKnobConfigE)
    - [`mDebugConfig`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig12mDebugConfigE)
    - [`mRecvPollPeriodMs`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig17mRecvPollPeriodMsE)
    - [`mMaxSeqIdleMicroseconds`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig23mMaxSeqIdleMicrosecondsE)
    - [`mSpeculativeDecodingConfig`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig26mSpeculativeDecodingConfigE)
    - [`mGuidedDecodingConfig`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig21mGuidedDecodingConfigE)
    - [`mAdditionalModelOutputs`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig23mAdditionalModelOutputsE)
    - [`mCacheTransceiverConfig`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig23mCacheTransceiverConfigE)
    - [`mGatherGenerationLogits`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig23mGatherGenerationLogitsE)
    - [`mPromptTableOffloading`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig22mPromptTableOffloadingE)
    - [`mEnableTrtOverlap`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig17mEnableTrtOverlapE)
    - [`mFailFastOnAttentionWindowTooLarge`](#_CPPv4N12tensorrt_llm8executor14ExecutorConfig34mFailFastOnAttentionWindowTooLargeE)
  + [`tensorrt_llm::executor::ExtendedRuntimePerfKnobConfig`](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfigE)
    - [`ExtendedRuntimePerfKnobConfig()`](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig29ExtendedRuntimePerfKnobConfigEbbb10SizeType32)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfigeqERK29ExtendedRuntimePerfKnobConfig)
    - [`getMultiBlockMode()`](#_CPPv4NK12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig17getMultiBlockModeEv)
    - [`getEnableContextFMHAFP32Acc()`](#_CPPv4NK12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig27getEnableContextFMHAFP32AccEv)
    - [`getCudaGraphMode()`](#_CPPv4NK12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig16getCudaGraphModeEv)
    - [`getCudaGraphCacheSize()`](#_CPPv4NK12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig21getCudaGraphCacheSizeEv)
    - [`setMultiBlockMode()`](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig17setMultiBlockModeEb)
    - [`setEnableContextFMHAFP32Acc()`](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig27setEnableContextFMHAFP32AccEb)
    - [`setCudaGraphMode()`](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig16setCudaGraphModeEb)
    - [`setCudaGraphCacheSize()`](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig21setCudaGraphCacheSizeE10SizeType32)
    - [`mMultiBlockMode`](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig15mMultiBlockModeE)
    - [`mEnableContextFMHAFP32Acc`](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig25mEnableContextFMHAFP32AccE)
    - [`mCudaGraphMode`](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig14mCudaGraphModeE)
    - [`mCudaGraphCacheSize`](#_CPPv4N12tensorrt_llm8executor29ExtendedRuntimePerfKnobConfig19mCudaGraphCacheSizeE)
  + [`tensorrt_llm::executor::ExternalDraftTokensConfig`](#_CPPv4N12tensorrt_llm8executor25ExternalDraftTokensConfigE)
    - [`ExternalDraftTokensConfig()`](#_CPPv4N12tensorrt_llm8executor25ExternalDraftTokensConfig25ExternalDraftTokensConfigE9VecTokensNSt8optionalI6TensorEERKNSt8optionalI9FloatTypeEERKNSt8optionalIbEE)
    - [`getTokens()`](#_CPPv4NK12tensorrt_llm8executor25ExternalDraftTokensConfig9getTokensEv)
    - [`getLogits()`](#_CPPv4NK12tensorrt_llm8executor25ExternalDraftTokensConfig9getLogitsEv)
    - [`getAcceptanceThreshold()`](#_CPPv4NK12tensorrt_llm8executor25ExternalDraftTokensConfig22getAcceptanceThresholdEv)
    - [`getFastLogits()`](#_CPPv4NK12tensorrt_llm8executor25ExternalDraftTokensConfig13getFastLogitsEv)
    - [`mTokens`](#_CPPv4N12tensorrt_llm8executor25ExternalDraftTokensConfig7mTokensE)
    - [`mLogits`](#_CPPv4N12tensorrt_llm8executor25ExternalDraftTokensConfig7mLogitsE)
    - [`mAcceptanceThreshold`](#_CPPv4N12tensorrt_llm8executor25ExternalDraftTokensConfig20mAcceptanceThresholdE)
    - [`mFastLogits`](#_CPPv4N12tensorrt_llm8executor25ExternalDraftTokensConfig11mFastLogitsE)
  + [`tensorrt_llm::executor::GuidedDecodingConfig`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfigE)
    - [`GuidedDecodingBackend`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig21GuidedDecodingBackendE)
      * [`kXGRAMMAR`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig21GuidedDecodingBackend9kXGRAMMARE)
      * [`kLLGUIDANCE`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig21GuidedDecodingBackend11kLLGUIDANCEE)
    - [`GuidedDecodingConfig()`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig20GuidedDecodingConfigE21GuidedDecodingBackendNSt8optionalINSt6vectorINSt6stringEEEEENSt8optionalINSt6stringEEENSt8optionalINSt6vectorI11TokenIdTypeEEEE)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor20GuidedDecodingConfigeqERK20GuidedDecodingConfig)
    - [`setBackend()`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig10setBackendERK21GuidedDecodingBackend)
    - [`getBackend()`](#_CPPv4NK12tensorrt_llm8executor20GuidedDecodingConfig10getBackendEv)
    - [`setEncodedVocab()`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig15setEncodedVocabERKNSt6vectorINSt6stringEEE)
    - [`getEncodedVocab()`](#_CPPv4NK12tensorrt_llm8executor20GuidedDecodingConfig15getEncodedVocabEv)
    - [`setTokenizerStr()`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig15setTokenizerStrERKNSt6stringE)
    - [`getTokenizerStr()`](#_CPPv4NK12tensorrt_llm8executor20GuidedDecodingConfig15getTokenizerStrEv)
    - [`setStopTokenIds()`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig15setStopTokenIdsERKNSt6vectorI11TokenIdTypeEE)
    - [`getStopTokenIds()`](#_CPPv4NK12tensorrt_llm8executor20GuidedDecodingConfig15getStopTokenIdsEv)
    - [`validate()`](#_CPPv4NK12tensorrt_llm8executor20GuidedDecodingConfig8validateEv)
    - [`mBackend`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig8mBackendE)
    - [`mEncodedVocab`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig13mEncodedVocabE)
    - [`mTokenizerStr`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig13mTokenizerStrE)
    - [`mStopTokenIds`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingConfig13mStopTokenIdsE)
  + [`tensorrt_llm::executor::GuidedDecodingParams`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParamsE)
    - [`GuideType`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams9GuideTypeE)
      * [`kJSON`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams9GuideType5kJSONE)
      * [`kJSON_SCHEMA`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams9GuideType12kJSON_SCHEMAE)
      * [`kREGEX`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams9GuideType6kREGEXE)
      * [`kEBNF_GRAMMAR`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams9GuideType13kEBNF_GRAMMARE)
      * [`kSTRUCTURAL_TAG`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams9GuideType15kSTRUCTURAL_TAGE)
    - [`GuidedDecodingParams()`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams20GuidedDecodingParamsE9GuideTypeNSt8optionalINSt6stringEEE)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor20GuidedDecodingParamseqERK20GuidedDecodingParams)
    - [`getGuideType()`](#_CPPv4NK12tensorrt_llm8executor20GuidedDecodingParams12getGuideTypeEv)
    - [`getGuide()`](#_CPPv4NK12tensorrt_llm8executor20GuidedDecodingParams8getGuideEv)
    - [`mGuideType`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams10mGuideTypeE)
    - [`mGuide`](#_CPPv4N12tensorrt_llm8executor20GuidedDecodingParams6mGuideE)
  + [`tensorrt_llm::executor::JsonSerialization`](#_CPPv4N12tensorrt_llm8executor17JsonSerializationE)
    - [`toJsonStr()`](#_CPPv4N12tensorrt_llm8executor17JsonSerialization9toJsonStrERK14IterationStats)
    - [`toJsonStr()`](#_CPPv4N12tensorrt_llm8executor17JsonSerialization9toJsonStrERK24RequestStatsPerIteration)
    - [`toJsonStr()`](#_CPPv4N12tensorrt_llm8executor17JsonSerialization9toJsonStrERK12RequestStats)
  + [`tensorrt_llm::executor::KvCacheConfig`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfigE)
    - [`KvCacheConfig()`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig13KvCacheConfigEbRKNSt8optionalI10SizeType32EERKNSt8optionalINSt6vectorI10SizeType32EEEERKNSt8optionalI10SizeType32EERKNSt8optionalI9FloatTypeEERKNSt8optionalI6size_tEEbRKNSt8optionalI9FloatTypeEENSt8optionalI17RetentionPriorityEE6size_tbbb10SizeType32RKNSt8optionalIN12tensorrt_llm7runtime15RuntimeDefaultsEEERK8uint64_t)
    - [`getEnableBlockReuse()`](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig19getEnableBlockReuseEv)
    - [`getEnablePartialReuse()`](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig21getEnablePartialReuseEv)
    - [`getCopyOnPartialReuse()`](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig21getCopyOnPartialReuseEv)
    - [`getMaxTokens()`](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig12getMaxTokensEv)
    - [`getMaxAttentionWindowVec()`](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig24getMaxAttentionWindowVecEv)
    - [`getSinkTokenLength()`](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig18getSinkTokenLengthEv)
    - [`getFreeGpuMemoryFraction()`](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig24getFreeGpuMemoryFractionEv)
    - [`getCrossKvCacheFraction()`](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig23getCrossKvCacheFractionEv)
    - [`getHostCacheSize()`](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig16getHostCacheSizeEv)
    - [`getOnboardBlocks()`](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig16getOnboardBlocksEv)
    - [`getSecondaryOffloadMinPriority()`](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig30getSecondaryOffloadMinPriorityEv)
    - [`getEventBufferMaxSize()`](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig21getEventBufferMaxSizeEv)
    - [`getUseUvm()`](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig9getUseUvmEv)
    - [`getAttentionDpEventsGatherPeriodMs()`](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig34getAttentionDpEventsGatherPeriodMsEv)
    - [`getMaxGpuTotalBytes()`](#_CPPv4NK12tensorrt_llm8executor13KvCacheConfig19getMaxGpuTotalBytesEv)
    - [`setEnableBlockReuse()`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig19setEnableBlockReuseEb)
    - [`setEnablePartialReuse()`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig21setEnablePartialReuseEb)
    - [`setCopyOnPartialReuse()`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig21setCopyOnPartialReuseEb)
    - [`setMaxTokens()`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig12setMaxTokensENSt8optionalI10SizeType32EE)
    - [`setMaxAttentionWindowVec()`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig24setMaxAttentionWindowVecENSt6vectorI10SizeType32EE)
    - [`setSinkTokenLength()`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig18setSinkTokenLengthE10SizeType32)
    - [`setFreeGpuMemoryFraction()`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig24setFreeGpuMemoryFractionE9FloatType)
    - [`setCrossKvCacheFraction()`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig23setCrossKvCacheFractionE9FloatType)
    - [`setHostCacheSize()`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig16setHostCacheSizeE6size_t)
    - [`setOnboardBlocks()`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig16setOnboardBlocksEb)
    - [`setSecondaryOffloadMinPriority()`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig30setSecondaryOffloadMinPriorityENSt8optionalI17RetentionPriorityEE)
    - [`setEventBufferMaxSize()`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig21setEventBufferMaxSizeE6size_t)
    - [`setUseUvm()`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig9setUseUvmEb)
    - [`setAttentionDpEventsGatherPeriodMs()`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig34setAttentionDpEventsGatherPeriodMsE10SizeType32)
    - [`setMaxGpuTotalBytes()`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig19setMaxGpuTotalBytesE8uint64_t)
    - [`fillEmptyFieldsFromRuntimeDefaults()`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig34fillEmptyFieldsFromRuntimeDefaultsERKN12tensorrt_llm7runtime15RuntimeDefaultsE)
    - [`kDefaultGpuMemFraction`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig22kDefaultGpuMemFractionE)
    - [`mEnableBlockReuse`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig17mEnableBlockReuseE)
    - [`mMaxTokens`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig10mMaxTokensE)
    - [`mMaxAttentionWindowVec`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig22mMaxAttentionWindowVecE)
    - [`mSinkTokenLength`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig16mSinkTokenLengthE)
    - [`mFreeGpuMemoryFraction`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig22mFreeGpuMemoryFractionE)
    - [`mCrossKvCacheFraction`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig21mCrossKvCacheFractionE)
    - [`mHostCacheSize`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig14mHostCacheSizeE)
    - [`mOnboardBlocks`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig14mOnboardBlocksE)
    - [`mSecondaryOffloadMinPriority`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig28mSecondaryOffloadMinPriorityE)
    - [`mEventBufferMaxSize`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig19mEventBufferMaxSizeE)
    - [`mEnablePartialReuse`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig19mEnablePartialReuseE)
    - [`mCopyOnPartialReuse`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig19mCopyOnPartialReuseE)
    - [`mUseUvm`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig7mUseUvmE)
    - [`mAttentionDpEventsGatherPeriodMs`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig32mAttentionDpEventsGatherPeriodMsE)
    - [`mMaxGpuTotalBytes`](#_CPPv4N12tensorrt_llm8executor13KvCacheConfig17mMaxGpuTotalBytesE)
  + [`tensorrt_llm::executor::KVCacheCreatedData`](#_CPPv4N12tensorrt_llm8executor18KVCacheCreatedDataE)
    - [`numBlocksPerCacheLevel`](#_CPPv4N12tensorrt_llm8executor18KVCacheCreatedData22numBlocksPerCacheLevelE)
  + [`tensorrt_llm::executor::KVCacheEvent`](#_CPPv4N12tensorrt_llm8executor12KVCacheEventE)
    - [`KVCacheEvent()`](#_CPPv4N12tensorrt_llm8executor12KVCacheEvent12KVCacheEventE6IdType16KVCacheEventData10SizeType32NSt8optionalI10SizeType32EE)
    - [`eventId`](#_CPPv4N12tensorrt_llm8executor12KVCacheEvent7eventIdE)
    - [`data`](#_CPPv4N12tensorrt_llm8executor12KVCacheEvent4dataE)
    - [`windowSize`](#_CPPv4N12tensorrt_llm8executor12KVCacheEvent10windowSizeE)
    - [`attentionDpRank`](#_CPPv4N12tensorrt_llm8executor12KVCacheEvent15attentionDpRankE)
  + [`tensorrt_llm::executor::KVCacheEventDiff`](#_CPPv4I0EN12tensorrt_llm8executor16KVCacheEventDiffE)
    - [`oldValue`](#_CPPv4N12tensorrt_llm8executor16KVCacheEventDiff8oldValueE)
    - [`newValue`](#_CPPv4N12tensorrt_llm8executor16KVCacheEventDiff8newValueE)
  + [`tensorrt_llm::executor::KVCacheEventManager`](#_CPPv4N12tensorrt_llm8executor19KVCacheEventManagerE)
    - [`KVCacheEventManager()`](#_CPPv4N12tensorrt_llm8executor19KVCacheEventManager19KVCacheEventManagerENSt10shared_ptrIN12tensorrt_llm13batch_manager16kv_cache_manager18BaseKVCacheManagerEEE)
    - [`getLatestEvents()`](#_CPPv4N12tensorrt_llm8executor19KVCacheEventManager15getLatestEventsENSt8optionalINSt6chrono12millisecondsEEE)
    - [`kvCacheManager`](#_CPPv4N12tensorrt_llm8executor19KVCacheEventManager14kvCacheManagerE)
  + [`tensorrt_llm::executor::KVCacheRemovedData`](#_CPPv4N12tensorrt_llm8executor18KVCacheRemovedDataE)
    - [`blockHashes`](#_CPPv4N12tensorrt_llm8executor18KVCacheRemovedData11blockHashesE)
  + [`tensorrt_llm::executor::KvCacheRetentionConfig`](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfigE)
    - [`KvCacheRetentionConfig()`](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig22KvCacheRetentionConfigEv)
    - [`KvCacheRetentionConfig()`](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig22KvCacheRetentionConfigERKNSt6vectorI25TokenRangeRetentionConfigEE17RetentionPriorityNSt8optionalINSt6chrono12millisecondsEEE19KvCacheTransferModeRKNSt6stringE)
    - [`getTokenRangeRetentionConfigs()`](#_CPPv4NK12tensorrt_llm8executor22KvCacheRetentionConfig29getTokenRangeRetentionConfigsEv)
    - [`getDecodeRetentionPriority()`](#_CPPv4NK12tensorrt_llm8executor22KvCacheRetentionConfig26getDecodeRetentionPriorityEv)
    - [`getDecodeDurationMs()`](#_CPPv4NK12tensorrt_llm8executor22KvCacheRetentionConfig19getDecodeDurationMsEv)
    - [`getTransferMode()`](#_CPPv4NK12tensorrt_llm8executor22KvCacheRetentionConfig15getTransferModeEv)
    - [`getDirectory()`](#_CPPv4NK12tensorrt_llm8executor22KvCacheRetentionConfig12getDirectoryEv)
    - [`getPerBlockRetentionPriorityDuration()`](#_CPPv4NK12tensorrt_llm8executor22KvCacheRetentionConfig36getPerBlockRetentionPriorityDurationE10SizeType3210SizeType32)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor22KvCacheRetentionConfigeqERK22KvCacheRetentionConfig)
    - [`kMinRetentionPriority`](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig21kMinRetentionPriorityE)
    - [`kMaxRetentionPriority`](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig21kMaxRetentionPriorityE)
    - [`kDefaultRetentionPriority`](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25kDefaultRetentionPriorityE)
    - [`mTokenRangeRetentionConfigs`](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig27mTokenRangeRetentionConfigsE)
    - [`mDecodeRetentionPriority`](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig24mDecodeRetentionPriorityE)
    - [`mDecodeDurationMs`](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig17mDecodeDurationMsE)
    - [`mTransferMode`](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig13mTransferModeE)
    - [`mDirectory`](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig10mDirectoryE)
    - [`tensorrt_llm::executor::KvCacheRetentionConfig::TokenRangeRetentionConfig`](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfigE)
      * [`TokenRangeRetentionConfig()`](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfig25TokenRangeRetentionConfigE10SizeType32NSt8optionalI10SizeType32EE17RetentionPriorityNSt8optionalINSt6chrono12millisecondsEEE)
      * [`operator==()`](#_CPPv4NK12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfigeqERK25TokenRangeRetentionConfig)
      * [`tokenStart`](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfig10tokenStartE)
      * [`tokenEnd`](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfig8tokenEndE)
      * [`priority`](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfig8priorityE)
      * [`durationMs`](#_CPPv4N12tensorrt_llm8executor22KvCacheRetentionConfig25TokenRangeRetentionConfig10durationMsE)
  + [`tensorrt_llm::executor::KVCacheStoredBlockData`](#_CPPv4N12tensorrt_llm8executor22KVCacheStoredBlockDataE)
    - [`KVCacheStoredBlockData()`](#_CPPv4N12tensorrt_llm8executor22KVCacheStoredBlockData22KVCacheStoredBlockDataE6IdTypeN12tensorrt_llm7runtime15VecUniqueTokensENSt8optionalIN12tensorrt_llm7runtime14LoraTaskIdTypeEEE10SizeType3210SizeType32)
    - [`blockHash`](#_CPPv4N12tensorrt_llm8executor22KVCacheStoredBlockData9blockHashE)
    - [`tokens`](#_CPPv4N12tensorrt_llm8executor22KVCacheStoredBlockData6tokensE)
    - [`loraId`](#_CPPv4N12tensorrt_llm8executor22KVCacheStoredBlockData6loraIdE)
    - [`cacheLevel`](#_CPPv4N12tensorrt_llm8executor22KVCacheStoredBlockData10cacheLevelE)
    - [`priority`](#_CPPv4N12tensorrt_llm8executor22KVCacheStoredBlockData8priorityE)
  + [`tensorrt_llm::executor::KVCacheStoredData`](#_CPPv4N12tensorrt_llm8executor17KVCacheStoredDataE)
    - [`parentHash`](#_CPPv4N12tensorrt_llm8executor17KVCacheStoredData10parentHashE)
    - [`blocks`](#_CPPv4N12tensorrt_llm8executor17KVCacheStoredData6blocksE)
  + [`tensorrt_llm::executor::KVCacheUpdatedData`](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedDataE)
    - [`KVCacheUpdatedData()`](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedData18KVCacheUpdatedDataE6IdType)
    - [`KVCacheUpdatedData()`](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedData18KVCacheUpdatedDataE6IdTypeNSt8optionalI16KVCacheEventDiffI10SizeType32EEENSt8optionalI16KVCacheEventDiffI10SizeType32EEE)
    - [`cacheLevelUpdated()`](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedData17cacheLevelUpdatedE10SizeType3210SizeType32)
    - [`priorityUpdated()`](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedData15priorityUpdatedE10SizeType3210SizeType32)
    - [`blockHash`](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedData9blockHashE)
    - [`cacheLevel`](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedData10cacheLevelE)
    - [`priority`](#_CPPv4N12tensorrt_llm8executor18KVCacheUpdatedData8priorityE)
  + [`tensorrt_llm::executor::LogitsPostProcessorConfig`](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfigE)
    - [`LogitsPostProcessorConfig()`](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfig25LogitsPostProcessorConfigENSt8optionalI22LogitsPostProcessorMapEENSt8optionalI26LogitsPostProcessorBatchedEEb)
    - [`getProcessorMap()`](#_CPPv4NK12tensorrt_llm8executor25LogitsPostProcessorConfig15getProcessorMapEv)
    - [`getProcessorBatched()`](#_CPPv4NK12tensorrt_llm8executor25LogitsPostProcessorConfig19getProcessorBatchedEv)
    - [`getReplicate()`](#_CPPv4NK12tensorrt_llm8executor25LogitsPostProcessorConfig12getReplicateEv)
    - [`setProcessorMap()`](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfig15setProcessorMapERK22LogitsPostProcessorMap)
    - [`setProcessorBatched()`](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfig19setProcessorBatchedERK26LogitsPostProcessorBatched)
    - [`setReplicate()`](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfig12setReplicateEb)
    - [`mProcessorMap`](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfig13mProcessorMapE)
    - [`mProcessorBatched`](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfig17mProcessorBatchedE)
    - [`mReplicate`](#_CPPv4N12tensorrt_llm8executor25LogitsPostProcessorConfig10mReplicateE)
  + [`tensorrt_llm::executor::LookaheadDecodingConfig`](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfigE)
    - [`LookaheadDecodingConfig()`](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig23LookaheadDecodingConfigE10SizeType3210SizeType3210SizeType32)
    - [`LookaheadDecodingConfig()`](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig23LookaheadDecodingConfigEv)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor23LookaheadDecodingConfigeqERK23LookaheadDecodingConfig)
    - [`get()`](#_CPPv4NK12tensorrt_llm8executor23LookaheadDecodingConfig3getEv)
    - [`getWindowSize()`](#_CPPv4NK12tensorrt_llm8executor23LookaheadDecodingConfig13getWindowSizeEv)
    - [`getNgramSize()`](#_CPPv4NK12tensorrt_llm8executor23LookaheadDecodingConfig12getNgramSizeEv)
    - [`getVerificationSetSize()`](#_CPPv4NK12tensorrt_llm8executor23LookaheadDecodingConfig22getVerificationSetSizeEv)
    - [`calculateSpeculativeResource()`](#_CPPv4NK12tensorrt_llm8executor23LookaheadDecodingConfig28calculateSpeculativeResourceEv)
    - [`isLE()`](#_CPPv4NK12tensorrt_llm8executor23LookaheadDecodingConfig4isLEERK23LookaheadDecodingConfig)
    - [`calculateSpeculativeResourceTuple()`](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig33calculateSpeculativeResourceTupleE10SizeType3210SizeType3210SizeType32)
    - [`isLegal()`](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig7isLegalE10SizeType3210SizeType3210SizeType32)
    - [`kDefaultLookaheadDecodingWindow`](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig31kDefaultLookaheadDecodingWindowE)
    - [`kDefaultLookaheadDecodingNgram`](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig30kDefaultLookaheadDecodingNgramE)
    - [`kDefaultLookaheadDecodingVerificationSet`](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig40kDefaultLookaheadDecodingVerificationSetE)
    - [`mWindowSize`](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig11mWindowSizeE)
    - [`mNgramSize`](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig10mNgramSizeE)
    - [`mVerificationSetSize`](#_CPPv4N12tensorrt_llm8executor23LookaheadDecodingConfig20mVerificationSetSizeE)
  + [`tensorrt_llm::executor::LoraConfig`](#_CPPv4N12tensorrt_llm8executor10LoraConfigE)
    - [`LoraConfig()`](#_CPPv4N12tensorrt_llm8executor10LoraConfig10LoraConfigE6IdTypeNSt8optionalI6TensorEENSt8optionalI6TensorEE)
    - [`getTaskId()`](#_CPPv4NK12tensorrt_llm8executor10LoraConfig9getTaskIdEv)
    - [`getWeights()`](#_CPPv4NK12tensorrt_llm8executor10LoraConfig10getWeightsEv)
    - [`getConfig()`](#_CPPv4NK12tensorrt_llm8executor10LoraConfig9getConfigEv)
    - [`mTaskId`](#_CPPv4N12tensorrt_llm8executor10LoraConfig7mTaskIdE)
    - [`mWeights`](#_CPPv4N12tensorrt_llm8executor10LoraConfig8mWeightsE)
    - [`mConfig`](#_CPPv4N12tensorrt_llm8executor10LoraConfig7mConfigE)
  + [`tensorrt_llm::executor::MropeConfig`](#_CPPv4N12tensorrt_llm8executor11MropeConfigE)
    - [`MropeConfig()`](#_CPPv4N12tensorrt_llm8executor11MropeConfig11MropeConfigE6Tensor10SizeType32)
    - [`getMRopeRotaryCosSin()`](#_CPPv4NK12tensorrt_llm8executor11MropeConfig20getMRopeRotaryCosSinEv)
    - [`getMRopePositionDeltas()`](#_CPPv4NK12tensorrt_llm8executor11MropeConfig22getMRopePositionDeltasEv)
    - [`mMRopeRotaryCosSin`](#_CPPv4N12tensorrt_llm8executor11MropeConfig18mMRopeRotaryCosSinE)
    - [`mMRopePositionDeltas`](#_CPPv4N12tensorrt_llm8executor11MropeConfig20mMRopePositionDeltasE)
  + [`tensorrt_llm::executor::MultimodalInput`](#_CPPv4N12tensorrt_llm8executor15MultimodalInputE)
    - [`MultimodalInput()`](#_CPPv4N12tensorrt_llm8executor15MultimodalInput15MultimodalInputENSt6vectorINSt6vectorI10SizeType32EEEENSt6vectorI10SizeType32EENSt6vectorI10SizeType32EE)
    - [`getMultimodalHashes()`](#_CPPv4NK12tensorrt_llm8executor15MultimodalInput19getMultimodalHashesEv)
    - [`getMultimodalPositions()`](#_CPPv4NK12tensorrt_llm8executor15MultimodalInput22getMultimodalPositionsEv)
    - [`getMultimodalLengths()`](#_CPPv4NK12tensorrt_llm8executor15MultimodalInput20getMultimodalLengthsEv)
    - [`mMultimodalHashes`](#_CPPv4N12tensorrt_llm8executor15MultimodalInput17mMultimodalHashesE)
    - [`mMultimodalPositions`](#_CPPv4N12tensorrt_llm8executor15MultimodalInput20mMultimodalPositionsE)
    - [`mMultimodalLengths`](#_CPPv4N12tensorrt_llm8executor15MultimodalInput18mMultimodalLengthsE)
  + [`tensorrt_llm::executor::OrchestratorConfig`](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfigE)
    - [`OrchestratorConfig()`](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfig18OrchestratorConfigEbNSt6stringENSt10shared_ptrIN3mpi7MpiCommEEEb)
    - [`getIsOrchestrator()`](#_CPPv4NK12tensorrt_llm8executor18OrchestratorConfig17getIsOrchestratorEv)
    - [`getWorkerExecutablePath()`](#_CPPv4NK12tensorrt_llm8executor18OrchestratorConfig23getWorkerExecutablePathEv)
    - [`getOrchLeaderComm()`](#_CPPv4NK12tensorrt_llm8executor18OrchestratorConfig17getOrchLeaderCommEv)
    - [`getSpawnProcesses()`](#_CPPv4NK12tensorrt_llm8executor18OrchestratorConfig17getSpawnProcessesEv)
    - [`setIsOrchestrator()`](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfig17setIsOrchestratorEb)
    - [`setWorkerExecutablePath()`](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfig23setWorkerExecutablePathERKNSt6stringE)
    - [`setOrchLeaderComm()`](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfig17setOrchLeaderCommERKNSt10shared_ptrIN3mpi7MpiCommEEE)
    - [`setSpawnProcesses()`](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfig17setSpawnProcessesEb)
    - [`mIsOrchestrator`](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfig15mIsOrchestratorE)
    - [`mWorkerExecutablePath`](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfig21mWorkerExecutablePathE)
    - [`mOrchLeaderComm`](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfig15mOrchLeaderCommE)
    - [`mSpawnProcesses`](#_CPPv4N12tensorrt_llm8executor18OrchestratorConfig15mSpawnProcessesE)
  + [`tensorrt_llm::executor::OutputConfig`](#_CPPv4N12tensorrt_llm8executor12OutputConfigE)
    - [`OutputConfig()`](#_CPPv4N12tensorrt_llm8executor12OutputConfig12OutputConfigEbbbbbbNSt8optionalINSt6vectorI21AdditionalModelOutputEEEE)
    - [`returnLogProbs`](#_CPPv4N12tensorrt_llm8executor12OutputConfig14returnLogProbsE)
    - [`returnContextLogits`](#_CPPv4N12tensorrt_llm8executor12OutputConfig19returnContextLogitsE)
    - [`returnGenerationLogits`](#_CPPv4N12tensorrt_llm8executor12OutputConfig22returnGenerationLogitsE)
    - [`excludeInputFromOutput`](#_CPPv4N12tensorrt_llm8executor12OutputConfig22excludeInputFromOutputE)
    - [`returnEncoderOutput`](#_CPPv4N12tensorrt_llm8executor12OutputConfig19returnEncoderOutputE)
    - [`returnPerfMetrics`](#_CPPv4N12tensorrt_llm8executor12OutputConfig17returnPerfMetricsE)
    - [`additionalModelOutputs`](#_CPPv4N12tensorrt_llm8executor12OutputConfig22additionalModelOutputsE)
  + [`tensorrt_llm::executor::ParallelConfig`](#_CPPv4N12tensorrt_llm8executor14ParallelConfigE)
    - [`ParallelConfig()`](#_CPPv4N12tensorrt_llm8executor14ParallelConfig14ParallelConfigE17CommunicationType17CommunicationModeNSt8optionalINSt6vectorI10SizeType32EEEENSt8optionalINSt6vectorI10SizeType32EEEERKNSt8optionalI18OrchestratorConfigEENSt8optionalI10SizeType32EE)
    - [`getCommunicationType()`](#_CPPv4NK12tensorrt_llm8executor14ParallelConfig20getCommunicationTypeEv)
    - [`getCommunicationMode()`](#_CPPv4NK12tensorrt_llm8executor14ParallelConfig20getCommunicationModeEv)
    - [`getDeviceIds()`](#_CPPv4NK12tensorrt_llm8executor14ParallelConfig12getDeviceIdsEv)
    - [`getParticipantIds()`](#_CPPv4NK12tensorrt_llm8executor14ParallelConfig17getParticipantIdsEv)
    - [`getOrchestratorConfig()`](#_CPPv4NK12tensorrt_llm8executor14ParallelConfig21getOrchestratorConfigEv)
    - [`getNumNodes()`](#_CPPv4NK12tensorrt_llm8executor14ParallelConfig11getNumNodesEv)
    - [`setCommunicationType()`](#_CPPv4N12tensorrt_llm8executor14ParallelConfig20setCommunicationTypeE17CommunicationType)
    - [`setCommunicationMode()`](#_CPPv4N12tensorrt_llm8executor14ParallelConfig20setCommunicationModeE17CommunicationMode)
    - [`setDeviceIds()`](#_CPPv4N12tensorrt_llm8executor14ParallelConfig12setDeviceIdsERKNSt6vectorI10SizeType32EE)
    - [`setParticipantIds()`](#_CPPv4N12tensorrt_llm8executor14ParallelConfig17setParticipantIdsERKNSt6vectorI10SizeType32EE)
    - [`setOrchestratorConfig()`](#_CPPv4N12tensorrt_llm8executor14ParallelConfig21setOrchestratorConfigERK18OrchestratorConfig)
    - [`setNumNodes()`](#_CPPv4N12tensorrt_llm8executor14ParallelConfig11setNumNodesE10SizeType32)
    - [`mCommType`](#_CPPv4N12tensorrt_llm8executor14ParallelConfig9mCommTypeE)
    - [`mCommMode`](#_CPPv4N12tensorrt_llm8executor14ParallelConfig9mCommModeE)
    - [`mDeviceIds`](#_CPPv4N12tensorrt_llm8executor14ParallelConfig10mDeviceIdsE)
    - [`mParticipantIds`](#_CPPv4N12tensorrt_llm8executor14ParallelConfig15mParticipantIdsE)
    - [`mOrchestratorConfig`](#_CPPv4N12tensorrt_llm8executor14ParallelConfig19mOrchestratorConfigE)
    - [`mNumNodes`](#_CPPv4N12tensorrt_llm8executor14ParallelConfig9mNumNodesE)
  + [`tensorrt_llm::executor::PeftCacheConfig`](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfigE)
    - [`PeftCacheConfig()`](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig15PeftCacheConfigE10SizeType3210SizeType3210SizeType3210SizeType3210SizeType3210SizeType3210SizeType3210SizeType3210SizeType32RKNSt8optionalIfEERKNSt8optionalI6size_tEERKNSt8optionalINSt6stringEEE)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfigeqERK15PeftCacheConfig)
    - [`getNumHostModuleLayer()`](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig21getNumHostModuleLayerEv)
    - [`getNumDeviceModuleLayer()`](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig23getNumDeviceModuleLayerEv)
    - [`getOptimalAdapterSize()`](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig21getOptimalAdapterSizeEv)
    - [`getMaxAdapterSize()`](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig17getMaxAdapterSizeEv)
    - [`getNumPutWorkers()`](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig16getNumPutWorkersEv)
    - [`getNumEnsureWorkers()`](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig19getNumEnsureWorkersEv)
    - [`getNumCopyStreams()`](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig17getNumCopyStreamsEv)
    - [`getMaxPagesPerBlockHost()`](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig23getMaxPagesPerBlockHostEv)
    - [`getMaxPagesPerBlockDevice()`](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig25getMaxPagesPerBlockDeviceEv)
    - [`getDeviceCachePercent()`](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig21getDeviceCachePercentEv)
    - [`getHostCacheSize()`](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig16getHostCacheSizeEv)
    - [`getLoraPrefetchDir()`](#_CPPv4NK12tensorrt_llm8executor15PeftCacheConfig18getLoraPrefetchDirEv)
    - [`kDefaultOptimalAdapterSize`](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig26kDefaultOptimalAdapterSizeE)
    - [`kDefaultMaxAdapterSize`](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig22kDefaultMaxAdapterSizeE)
    - [`kDefaultMaxPagesPerBlockHost`](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig28kDefaultMaxPagesPerBlockHostE)
    - [`kDefaultMaxPagesPerBlockDevice`](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig30kDefaultMaxPagesPerBlockDeviceE)
    - [`mNumHostModuleLayer`](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig19mNumHostModuleLayerE)
    - [`mNumDeviceModuleLayer`](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig21mNumDeviceModuleLayerE)
    - [`mOptimalAdapterSize`](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig19mOptimalAdapterSizeE)
    - [`mMaxAdapterSize`](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig15mMaxAdapterSizeE)
    - [`mNumPutWorkers`](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig14mNumPutWorkersE)
    - [`mNumEnsureWorkers`](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig17mNumEnsureWorkersE)
    - [`mNumCopyStreams`](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig15mNumCopyStreamsE)
    - [`mMaxPagesPerBlockHost`](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig21mMaxPagesPerBlockHostE)
    - [`mMaxPagesPerBlockDevice`](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig23mMaxPagesPerBlockDeviceE)
    - [`mDeviceCachePercent`](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig19mDeviceCachePercentE)
    - [`mHostCacheSize`](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig14mHostCacheSizeE)
    - [`mLoraPrefetchDir`](#_CPPv4N12tensorrt_llm8executor15PeftCacheConfig16mLoraPrefetchDirE)
  + [`tensorrt_llm::executor::PromptTuningConfig`](#_CPPv4N12tensorrt_llm8executor18PromptTuningConfigE)
    - [`PromptTuningConfig()`](#_CPPv4N12tensorrt_llm8executor18PromptTuningConfig18PromptTuningConfigE6TensorNSt8optionalI16VecTokenExtraIdsEE)
    - [`getEmbeddingTable()`](#_CPPv4NK12tensorrt_llm8executor18PromptTuningConfig17getEmbeddingTableEv)
    - [`getInputTokenExtraIds()`](#_CPPv4NK12tensorrt_llm8executor18PromptTuningConfig21getInputTokenExtraIdsEv)
    - [`mEmbeddingTable`](#_CPPv4N12tensorrt_llm8executor18PromptTuningConfig15mEmbeddingTableE)
    - [`mInputTokenExtraIds`](#_CPPv4N12tensorrt_llm8executor18PromptTuningConfig19mInputTokenExtraIdsE)
  + [`tensorrt_llm::executor::Request`](#_CPPv4N12tensorrt_llm8executor7RequestE)
    - [`Request()`](#_CPPv4N12tensorrt_llm8executor7Request7RequestE9VecTokens10SizeType32bRK14SamplingConfigRK12OutputConfigRKNSt8optionalI10SizeType32EERKNSt8optionalI10SizeType32EENSt8optionalINSt6vectorI10SizeType32EEEENSt8optionalINSt4listI9VecTokensEEEENSt8optionalINSt4listI9VecTokensEEEENSt8optionalI6TensorEENSt8optionalI25ExternalDraftTokensConfigEENSt8optionalI18PromptTuningConfigEENSt8optionalI15MultimodalInputEENSt8optionalI6TensorEENSt8optionalI11MropeConfigEENSt8optionalI10LoraConfigEENSt8optionalI23LookaheadDecodingConfigEENSt8optionalI22KvCacheRetentionConfigEENSt8optionalINSt6stringEEENSt8optionalI19LogitsPostProcessorEENSt8optionalI9VecTokensEENSt8optionalI6IdTypeEEb12PriorityType11RequestTypeNSt8optionalI18ContextPhaseParamsEENSt8optionalI6TensorEENSt8optionalI10SizeType32EENSt8optionalI6TensorEE10SizeType32NSt8optionalI11EagleConfigEENSt8optionalI6TensorEENSt8optionalI20GuidedDecodingParamsEENSt8optionalI10SizeType32EENSt8optionalI16MillisecondsTypeEENSt8optionalI15CacheSaltIDTypeEE)
    - [`Request()`](#_CPPv4N12tensorrt_llm8executor7Request7RequestERK7Request)
    - [`Request()`](#_CPPv4N12tensorrt_llm8executor7Request7RequestERR7Request)
    - [`operator=()`](#_CPPv4N12tensorrt_llm8executor7RequestaSERK7Request)
    - [`operator=()`](#_CPPv4N12tensorrt_llm8executor7RequestaSERR7Request)
    - [`~Request()`](#_CPPv4N12tensorrt_llm8executor7RequestD0Ev)
    - [`getInputTokenIds()`](#_CPPv4NK12tensorrt_llm8executor7Request16getInputTokenIdsEv)
    - [`getMaxTokens()`](#_CPPv4NK12tensorrt_llm8executor7Request12getMaxTokensEv)
    - [`getStreaming()`](#_CPPv4NK12tensorrt_llm8executor7Request12getStreamingEv)
    - [`getSamplingConfig()`](#_CPPv4NK12tensorrt_llm8executor7Request17getSamplingConfigEv)
    - [`getOutputConfig()`](#_CPPv4NK12tensorrt_llm8executor7Request15getOutputConfigEv)
    - [`getEndId()`](#_CPPv4NK12tensorrt_llm8executor7Request8getEndIdEv)
    - [`getPadId()`](#_CPPv4NK12tensorrt_llm8executor7Request8getPadIdEv)
    - [`getPositionIds()`](#_CPPv4NK12tensorrt_llm8executor7Request14getPositionIdsEv)
    - [`getBadWords()`](#_CPPv4NK12tensorrt_llm8executor7Request11getBadWordsEv)
    - [`getStopWords()`](#_CPPv4NK12tensorrt_llm8executor7Request12getStopWordsEv)
    - [`getEmbeddingBias()`](#_CPPv4NK12tensorrt_llm8executor7Request16getEmbeddingBiasEv)
    - [`getExternalDraftTokensConfig()`](#_CPPv4NK12tensorrt_llm8executor7Request28getExternalDraftTokensConfigEv)
    - [`getPromptTuningConfig()`](#_CPPv4NK12tensorrt_llm8executor7Request21getPromptTuningConfigEv)
    - [`getMultimodalInput()`](#_CPPv4NK12tensorrt_llm8executor7Request18getMultimodalInputEv)
    - [`getMultimodalEmbedding()`](#_CPPv4NK12tensorrt_llm8executor7Request22getMultimodalEmbeddingEv)
    - [`getMropeConfig()`](#_CPPv4NK12tensorrt_llm8executor7Request14getMropeConfigEv)
    - [`getLoraConfig()`](#_CPPv4NK12tensorrt_llm8executor7Request13getLoraConfigEv)
    - [`getLookaheadConfig()`](#_CPPv4NK12tensorrt_llm8executor7Request18getLookaheadConfigEv)
    - [`getKvCacheRetentionConfig()`](#_CPPv4NK12tensorrt_llm8executor7Request25getKvCacheRetentionConfigEv)
    - [`getLogitsPostProcessorName()`](#_CPPv4NK12tensorrt_llm8executor7Request26getLogitsPostProcessorNameEv)
    - [`getLogitsPostProcessor()`](#_CPPv4NK12tensorrt_llm8executor7Request22getLogitsPostProcessorEv)
    - [`getEncoderInputTokenIds()`](#_CPPv4NK12tensorrt_llm8executor7Request23getEncoderInputTokenIdsEv)
    - [`getClientId()`](#_CPPv4NK12tensorrt_llm8executor7Request11getClientIdEv)
    - [`getPriority()`](#_CPPv4NK12tensorrt_llm8executor7Request11getPriorityEv)
    - [`getReturnAllGeneratedTokens()`](#_CPPv4NK12tensorrt_llm8executor7Request27getReturnAllGeneratedTokensEv)
    - [`getContextPhaseParams()`](#_CPPv4NK12tensorrt_llm8executor7Request21getContextPhaseParamsEv)
    - [`getEncoderInputFeatures()`](#_CPPv4NK12tensorrt_llm8executor7Request23getEncoderInputFeaturesEv)
    - [`getEncoderOutputLength()`](#_CPPv4NK12tensorrt_llm8executor7Request22getEncoderOutputLengthEv)
    - [`getCrossAttentionMask()`](#_CPPv4NK12tensorrt_llm8executor7Request21getCrossAttentionMaskEv)
    - [`getRequestType()`](#_CPPv4NK12tensorrt_llm8executor7Request14getRequestTypeEv)
    - [`getEagleConfig()`](#_CPPv4NK12tensorrt_llm8executor7Request14getEagleConfigEv)
    - [`getSkipCrossAttnBlocks()`](#_CPPv4NK12tensorrt_llm8executor7Request22getSkipCrossAttnBlocksEv)
    - [`getGuidedDecodingParams()`](#_CPPv4NK12tensorrt_llm8executor7Request23getGuidedDecodingParamsEv)
    - [`getLanguageAdapterUid()`](#_CPPv4NK12tensorrt_llm8executor7Request21getLanguageAdapterUidEv)
    - [`getAllottedTimeMs()`](#_CPPv4NK12tensorrt_llm8executor7Request17getAllottedTimeMsEv)
    - [`getCacheSaltID()`](#_CPPv4NK12tensorrt_llm8executor7Request14getCacheSaltIDEv)
    - [`getAdditionalOutputNames()`](#_CPPv4NK12tensorrt_llm8executor7Request24getAdditionalOutputNamesEv)
    - [`setStreaming()`](#_CPPv4N12tensorrt_llm8executor7Request12setStreamingEb)
    - [`setSamplingConfig()`](#_CPPv4N12tensorrt_llm8executor7Request17setSamplingConfigERK14SamplingConfig)
    - [`setOutputConfig()`](#_CPPv4N12tensorrt_llm8executor7Request15setOutputConfigERK12OutputConfig)
    - [`setEndId()`](#_CPPv4N12tensorrt_llm8executor7Request8setEndIdE10SizeType32)
    - [`setPadId()`](#_CPPv4N12tensorrt_llm8executor7Request8setPadIdE10SizeType32)
    - [`setPositionIds()`](#_CPPv4N12tensorrt_llm8executor7Request14setPositionIdsERKNSt6vectorI10SizeType32EE)
    - [`setBadWords()`](#_CPPv4N12tensorrt_llm8executor7Request11setBadWordsERKNSt4listI9VecTokensEE)
    - [`setStopWords()`](#_CPPv4N12tensorrt_llm8executor7Request12setStopWordsERKNSt4listI9VecTokensEE)
    - [`setEmbeddingBias()`](#_CPPv4N12tensorrt_llm8executor7Request16setEmbeddingBiasERK6Tensor)
    - [`setExternalDraftTokensConfig()`](#_CPPv4N12tensorrt_llm8executor7Request28setExternalDraftTokensConfigERK25ExternalDraftTokensConfig)
    - [`setPromptTuningConfig()`](#_CPPv4N12tensorrt_llm8executor7Request21setPromptTuningConfigERK18PromptTuningConfig)
    - [`setMultimodalEmbedding()`](#_CPPv4N12tensorrt_llm8executor7Request22setMultimodalEmbeddingERK6Tensor)
    - [`setMultimodalInput()`](#_CPPv4N12tensorrt_llm8executor7Request18setMultimodalInputERK15MultimodalInput)
    - [`setMropeConfig()`](#_CPPv4N12tensorrt_llm8executor7Request14setMropeConfigERK11MropeConfig)
    - [`setLoraConfig()`](#_CPPv4N12tensorrt_llm8executor7Request13setLoraConfigERK10LoraConfig)
    - [`setLookaheadConfig()`](#_CPPv4N12tensorrt_llm8executor7Request18setLookaheadConfigERK23LookaheadDecodingConfig)
    - [`setKvCacheRetentionConfig()`](#_CPPv4N12tensorrt_llm8executor7Request25setKvCacheRetentionConfigERK22KvCacheRetentionConfig)
    - [`setLogitsPostProcessorName()`](#_CPPv4N12tensorrt_llm8executor7Request26setLogitsPostProcessorNameERKNSt6stringE)
    - [`setLogitsPostProcessor()`](#_CPPv4N12tensorrt_llm8executor7Request22setLogitsPostProcessorERKNSt8optionalI19LogitsPostProcessorEE)
    - [`setEncoderInputTokenIds()`](#_CPPv4N12tensorrt_llm8executor7Request23setEncoderInputTokenIdsERK9VecTokens)
    - [`setClientId()`](#_CPPv4N12tensorrt_llm8executor7Request11setClientIdE6IdType)
    - [`setPriority()`](#_CPPv4N12tensorrt_llm8executor7Request11setPriorityE12PriorityType)
    - [`setReturnAllGeneratedTokens()`](#_CPPv4N12tensorrt_llm8executor7Request27setReturnAllGeneratedTokensEb)
    - [`setRequestType()`](#_CPPv4N12tensorrt_llm8executor7Request14setRequestTypeERK11RequestType)
    - [`setContextPhaseParams()`](#_CPPv4N12tensorrt_llm8executor7Request21setContextPhaseParamsE18ContextPhaseParams)
    - [`setEncoderInputFeatures()`](#_CPPv4N12tensorrt_llm8executor7Request23setEncoderInputFeaturesE6Tensor)
    - [`setEncoderOutputLength()`](#_CPPv4N12tensorrt_llm8executor7Request22setEncoderOutputLengthE10SizeType32)
    - [`setCrossAttentionMask()`](#_CPPv4N12tensorrt_llm8executor7Request21setCrossAttentionMaskE6Tensor)
    - [`setEagleConfig()`](#_CPPv4N12tensorrt_llm8executor7Request14setEagleConfigERKNSt8optionalI11EagleConfigEE)
    - [`setSkipCrossAttnBlocks()`](#_CPPv4N12tensorrt_llm8executor7Request22setSkipCrossAttnBlocksE6Tensor)
    - [`setGuidedDecodingParams()`](#_CPPv4N12tensorrt_llm8executor7Request23setGuidedDecodingParamsERK20GuidedDecodingParams)
    - [`setLanguageAdapterUid()`](#_CPPv4N12tensorrt_llm8executor7Request21setLanguageAdapterUidE10SizeType32)
    - [`setAllottedTimeMs()`](#_CPPv4N12tensorrt_llm8executor7Request17setAllottedTimeMsE16MillisecondsType)
    - [`setCacheSaltID()`](#_CPPv4N12tensorrt_llm8executor7Request14setCacheSaltIDE15CacheSaltIDType)
    - [`kDefaultPriority`](#_CPPv4N12tensorrt_llm8executor7Request16kDefaultPriorityE)
    - [`kBatchedPostProcessorName`](#_CPPv4N12tensorrt_llm8executor7Request25kBatchedPostProcessorNameE)
    - [`kDynamicPostProcessorNamePrefix`](#_CPPv4N12tensorrt_llm8executor7Request31kDynamicPostProcessorNamePrefixE)
    - [`mImpl`](#_CPPv4N12tensorrt_llm8executor7Request5mImplE)
  + [`tensorrt_llm::executor::Response`](#_CPPv4N12tensorrt_llm8executor8ResponseE)
    - [`Response()`](#_CPPv4N12tensorrt_llm8executor8Response8ResponseE6IdTypeNSt6stringENSt8optionalI6IdTypeEE)
    - [`Response()`](#_CPPv4N12tensorrt_llm8executor8Response8ResponseE6IdType6ResultNSt8optionalI6IdTypeEE)
    - [`~Response()`](#_CPPv4N12tensorrt_llm8executor8ResponseD0Ev)
    - [`Response()`](#_CPPv4N12tensorrt_llm8executor8Response8ResponseERK8Response)
    - [`Response()`](#_CPPv4N12tensorrt_llm8executor8Response8ResponseERR8Response)
    - [`operator=()`](#_CPPv4N12tensorrt_llm8executor8ResponseaSERK8Response)
    - [`operator=()`](#_CPPv4N12tensorrt_llm8executor8ResponseaSERR8Response)
    - [`getRequestId()`](#_CPPv4NK12tensorrt_llm8executor8Response12getRequestIdEv)
    - [`getClientId()`](#_CPPv4NK12tensorrt_llm8executor8Response11getClientIdEv)
    - [`hasError()`](#_CPPv4NK12tensorrt_llm8executor8Response8hasErrorEv)
    - [`getErrorMsg()`](#_CPPv4NK12tensorrt_llm8executor8Response11getErrorMsgEv)
    - [`getResult()`](#_CPPv4NK12tensorrt_llm8executor8Response9getResultEv)
    - [`mImpl`](#_CPPv4N12tensorrt_llm8executor8Response5mImplE)
  + [`tensorrt_llm::executor::Result`](#_CPPv4N12tensorrt_llm8executor6ResultE)
    - [`isFinal`](#_CPPv4N12tensorrt_llm8executor6Result7isFinalE)
    - [`outputTokenIds`](#_CPPv4N12tensorrt_llm8executor6Result14outputTokenIdsE)
    - [`cumLogProbs`](#_CPPv4N12tensorrt_llm8executor6Result11cumLogProbsE)
    - [`logProbs`](#_CPPv4N12tensorrt_llm8executor6Result8logProbsE)
    - [`contextLogits`](#_CPPv4N12tensorrt_llm8executor6Result13contextLogitsE)
    - [`generationLogits`](#_CPPv4N12tensorrt_llm8executor6Result16generationLogitsE)
    - [`specDecFastLogitsInfo`](#_CPPv4N12tensorrt_llm8executor6Result21specDecFastLogitsInfoE)
    - [`encoderOutput`](#_CPPv4N12tensorrt_llm8executor6Result13encoderOutputE)
    - [`finishReasons`](#_CPPv4N12tensorrt_llm8executor6Result13finishReasonsE)
    - [`contextPhaseParams`](#_CPPv4N12tensorrt_llm8executor6Result18contextPhaseParamsE)
    - [`decodingIter`](#_CPPv4N12tensorrt_llm8executor6Result12decodingIterE)
    - [`avgDecodedTokensPerIter`](#_CPPv4N12tensorrt_llm8executor6Result23avgDecodedTokensPerIterE)
    - [`sequenceIndex`](#_CPPv4N12tensorrt_llm8executor6Result13sequenceIndexE)
    - [`isSequenceFinal`](#_CPPv4N12tensorrt_llm8executor6Result15isSequenceFinalE)
    - [`requestPerfMetrics`](#_CPPv4N12tensorrt_llm8executor6Result18requestPerfMetricsE)
    - [`additionalOutputs`](#_CPPv4N12tensorrt_llm8executor6Result17additionalOutputsE)
  + [`tensorrt_llm::executor::RetentionPriorityAndDuration`](#_CPPv4N12tensorrt_llm8executor28RetentionPriorityAndDurationE)
    - [`RetentionPriorityAndDuration()`](#_CPPv4N12tensorrt_llm8executor28RetentionPriorityAndDuration28RetentionPriorityAndDurationERKNSt8optionalI17RetentionPriorityEERKNSt8optionalINSt6chrono12millisecondsEEE)
    - [`retentionPriority`](#_CPPv4N12tensorrt_llm8executor28RetentionPriorityAndDuration17retentionPriorityE)
    - [`durationMs`](#_CPPv4N12tensorrt_llm8executor28RetentionPriorityAndDuration10durationMsE)
  + [`tensorrt_llm::executor::SamplingConfig`](#_CPPv4N12tensorrt_llm8executor14SamplingConfigE)
    - [`SamplingConfig()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig14SamplingConfigE10SizeType32RKNSt8optionalI10SizeType32EERKNSt8optionalI9FloatTypeEERKNSt8optionalI9FloatTypeEERKNSt8optionalI11TokenIdTypeEERKNSt8optionalI9FloatTypeEERKNSt8optionalI14RandomSeedTypeEERKNSt8optionalI9FloatTypeEERKNSt8optionalI10SizeType32EERKNSt8optionalI9FloatTypeEERKNSt8optionalI9FloatTypeEERKNSt8optionalI9FloatTypeEERKNSt8optionalI9FloatTypeEERKNSt8optionalI9FloatTypeEERKNSt8optionalI10SizeType32EERKNSt8optionalI10SizeType32EERKNSt8optionalI10SizeType32EERKNSt8optionalI9FloatTypeEERKNSt8optionalINSt6vectorI10SizeType32EEEE)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfigeqERK14SamplingConfig)
    - [`getBeamWidth()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig12getBeamWidthEv)
    - [`getNumReturnBeams()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig17getNumReturnBeamsEv)
    - [`getTopK()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig7getTopKEv)
    - [`getTopP()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig7getTopPEv)
    - [`getTopPMin()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig10getTopPMinEv)
    - [`getTopPResetIds()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig15getTopPResetIdsEv)
    - [`getTopPDecay()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig12getTopPDecayEv)
    - [`getSeed()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig7getSeedEv)
    - [`getTemperature()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig14getTemperatureEv)
    - [`getMinTokens()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig12getMinTokensEv)
    - [`getBeamSearchDiversityRate()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig26getBeamSearchDiversityRateEv)
    - [`getRepetitionPenalty()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig20getRepetitionPenaltyEv)
    - [`getPresencePenalty()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig18getPresencePenaltyEv)
    - [`getFrequencyPenalty()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig19getFrequencyPenaltyEv)
    - [`getLengthPenalty()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig16getLengthPenaltyEv)
    - [`getEarlyStopping()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig16getEarlyStoppingEv)
    - [`getNoRepeatNgramSize()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig20getNoRepeatNgramSizeEv)
    - [`getNumReturnSequences()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig21getNumReturnSequencesEv)
    - [`getMinP()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig7getMinPEv)
    - [`getBeamWidthArray()`](#_CPPv4NK12tensorrt_llm8executor14SamplingConfig17getBeamWidthArrayEv)
    - [`setBeamWidth()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig12setBeamWidthE10SizeType32)
    - [`setTopK()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig7setTopKERKNSt8optionalI10SizeType32EE)
    - [`setTopP()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig7setTopPERKNSt8optionalI9FloatTypeEE)
    - [`setTopPMin()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig10setTopPMinERKNSt8optionalI9FloatTypeEE)
    - [`setTopPResetIds()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig15setTopPResetIdsERKNSt8optionalI11TokenIdTypeEE)
    - [`setTopPDecay()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig12setTopPDecayERKNSt8optionalI9FloatTypeEE)
    - [`setSeed()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig7setSeedERKNSt8optionalI14RandomSeedTypeEE)
    - [`setTemperature()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig14setTemperatureERKNSt8optionalI9FloatTypeEE)
    - [`setMinTokens()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig12setMinTokensERKNSt8optionalI10SizeType32EE)
    - [`setBeamSearchDiversityRate()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig26setBeamSearchDiversityRateERKNSt8optionalI9FloatTypeEE)
    - [`setRepetitionPenalty()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig20setRepetitionPenaltyERKNSt8optionalI9FloatTypeEE)
    - [`setPresencePenalty()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig18setPresencePenaltyERKNSt8optionalI9FloatTypeEE)
    - [`setFrequencyPenalty()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig19setFrequencyPenaltyERKNSt8optionalI9FloatTypeEE)
    - [`setLengthPenalty()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig16setLengthPenaltyERKNSt8optionalI9FloatTypeEE)
    - [`setEarlyStopping()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig16setEarlyStoppingERKNSt8optionalI10SizeType32EE)
    - [`setNoRepeatNgramSize()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig20setNoRepeatNgramSizeERKNSt8optionalI10SizeType32EE)
    - [`setNumReturnSequences()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig21setNumReturnSequencesERKNSt8optionalI10SizeType32EE)
    - [`setMinP()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig7setMinPERKNSt8optionalI9FloatTypeEE)
    - [`setBeamWidthArray()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig17setBeamWidthArrayERKNSt8optionalINSt6vectorI10SizeType32EEEE)
    - [`updateNumReturnBeams()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig20updateNumReturnBeamsEv)
    - [`mBeamWidth`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig10mBeamWidthE)
    - [`mTopK`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig5mTopKE)
    - [`mTopP`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig5mTopPE)
    - [`mTopPMin`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig8mTopPMinE)
    - [`mTopPResetIds`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig13mTopPResetIdsE)
    - [`mTopPDecay`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig10mTopPDecayE)
    - [`mSeed`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig5mSeedE)
    - [`mTemperature`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig12mTemperatureE)
    - [`mMinTokens`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig10mMinTokensE)
    - [`mBeamSearchDiversityRate`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig24mBeamSearchDiversityRateE)
    - [`mRepetitionPenalty`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig18mRepetitionPenaltyE)
    - [`mPresencePenalty`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig16mPresencePenaltyE)
    - [`mFrequencyPenalty`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig17mFrequencyPenaltyE)
    - [`mLengthPenalty`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig14mLengthPenaltyE)
    - [`mEarlyStopping`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig14mEarlyStoppingE)
    - [`mNoRepeatNgramSize`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig18mNoRepeatNgramSizeE)
    - [`mNumReturnSequences`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig19mNumReturnSequencesE)
    - [`mNumReturnBeams`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig15mNumReturnBeamsE)
    - [`mMinP`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig5mMinPE)
    - [`mBeamWidthArray`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig15mBeamWidthArrayE)
    - [`checkBeamWidth()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig14checkBeamWidthE10SizeType32)
    - [`checkTopK()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig9checkTopKERKNSt8optionalI9FloatTypeEE)
    - [`checkTopP()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig9checkTopPERKNSt8optionalI9FloatTypeEE)
    - [`checkTopPMin()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig12checkTopPMinERKNSt8optionalI9FloatTypeEE)
    - [`checkTopPResetIds()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig17checkTopPResetIdsERKNSt8optionalI11TokenIdTypeEE)
    - [`checkTopPDecay()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig14checkTopPDecayERKNSt8optionalI9FloatTypeEE)
    - [`checkTemperature()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig16checkTemperatureERKNSt8optionalI9FloatTypeEE)
    - [`checkMinTokens()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig14checkMinTokensERKNSt8optionalI10SizeType32EE)
    - [`checkBeamSearchDiversityRate()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig28checkBeamSearchDiversityRateERKNSt8optionalI9FloatTypeEE)
    - [`checkRepetitionPenalty()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig22checkRepetitionPenaltyERKNSt8optionalI9FloatTypeEE)
    - [`checkLengthPenalty()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig18checkLengthPenaltyERKNSt8optionalI9FloatTypeEE)
    - [`checkEarlyStopping()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig18checkEarlyStoppingERKNSt8optionalI10SizeType32EE)
    - [`checkNoRepeatNgramSize()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig22checkNoRepeatNgramSizeERKNSt8optionalI10SizeType32EE)
    - [`checkNumReturnSequences()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig23checkNumReturnSequencesERKNSt8optionalI10SizeType32EE10SizeType32)
    - [`checkMinP()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig9checkMinPERKNSt8optionalI9FloatTypeEE)
    - [`checkBeamWidthArray()`](#_CPPv4N12tensorrt_llm8executor14SamplingConfig19checkBeamWidthArrayERKNSt8optionalINSt6vectorI10SizeType32EEEEK10SizeType32)
  + [`tensorrt_llm::executor::SchedulerConfig`](#_CPPv4N12tensorrt_llm8executor15SchedulerConfigE)
    - [`SchedulerConfig()`](#_CPPv4N12tensorrt_llm8executor15SchedulerConfig15SchedulerConfigE23CapacitySchedulerPolicyNSt8optionalI21ContextChunkingPolicyEENSt8optionalI18DynamicBatchConfigEE)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor15SchedulerConfigeqERK15SchedulerConfig)
    - [`getCapacitySchedulerPolicy()`](#_CPPv4NK12tensorrt_llm8executor15SchedulerConfig26getCapacitySchedulerPolicyEv)
    - [`getContextChunkingPolicy()`](#_CPPv4NK12tensorrt_llm8executor15SchedulerConfig24getContextChunkingPolicyEv)
    - [`getDynamicBatchConfig()`](#_CPPv4NK12tensorrt_llm8executor15SchedulerConfig21getDynamicBatchConfigEv)
    - [`mCapacitySchedulerPolicy`](#_CPPv4N12tensorrt_llm8executor15SchedulerConfig24mCapacitySchedulerPolicyE)
    - [`mContextChunkingPolicy`](#_CPPv4N12tensorrt_llm8executor15SchedulerConfig22mContextChunkingPolicyE)
    - [`mDynamicBatchConfig`](#_CPPv4N12tensorrt_llm8executor15SchedulerConfig19mDynamicBatchConfigE)
  + [`tensorrt_llm::executor::SpeculativeDecodingConfig`](#_CPPv4N12tensorrt_llm8executor25SpeculativeDecodingConfigE)
    - [`SpeculativeDecodingConfig()`](#_CPPv4N12tensorrt_llm8executor25SpeculativeDecodingConfig25SpeculativeDecodingConfigEb)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor25SpeculativeDecodingConfigeqERK25SpeculativeDecodingConfig)
    - [`fastLogits`](#_CPPv4N12tensorrt_llm8executor25SpeculativeDecodingConfig10fastLogitsE)
  + [`tensorrt_llm::executor::SpeculativeDecodingFastLogitsInfo`](#_CPPv4N12tensorrt_llm8executor33SpeculativeDecodingFastLogitsInfoE)
    - [`toTensor()`](#_CPPv4NK12tensorrt_llm8executor33SpeculativeDecodingFastLogitsInfo8toTensorEv)
    - [`draftRequestId`](#_CPPv4N12tensorrt_llm8executor33SpeculativeDecodingFastLogitsInfo14draftRequestIdE)
    - [`draftParticipantId`](#_CPPv4N12tensorrt_llm8executor33SpeculativeDecodingFastLogitsInfo18draftParticipantIdE)
  + [`tensorrt_llm::mpi`](#_CPPv4N12tensorrt_llm3mpiE)
* [types.h](#types-h)
  + [`TensorPtr`](#_CPPv4N12tensorrt_llm8executor9TensorPtrE)
  + [`SizeType32`](#_CPPv4N12tensorrt_llm8executor10SizeType32E)
  + [`SizeType64`](#_CPPv4N12tensorrt_llm8executor10SizeType64E)
  + [`FloatType`](#_CPPv4N12tensorrt_llm8executor9FloatTypeE)
  + [`TokenIdType`](#_CPPv4N12tensorrt_llm8executor11TokenIdTypeE)
  + [`VecTokens`](#_CPPv4N12tensorrt_llm8executor9VecTokensE)
  + [`BeamTokens`](#_CPPv4N12tensorrt_llm8executor10BeamTokensE)
  + [`IdType`](#_CPPv4N12tensorrt_llm8executor6IdTypeE)
  + [`VecTokenExtraIds`](#_CPPv4N12tensorrt_llm8executor16VecTokenExtraIdsE)
  + [`IterationType`](#_CPPv4N12tensorrt_llm8executor13IterationTypeE)
  + [`RandomSeedType`](#_CPPv4N12tensorrt_llm8executor14RandomSeedTypeE)
  + [`VecLogProbs`](#_CPPv4N12tensorrt_llm8executor11VecLogProbsE)
  + [`StreamPtr`](#_CPPv4N12tensorrt_llm8executor9StreamPtrE)
  + [`MillisecondsType`](#_CPPv4N12tensorrt_llm8executor16MillisecondsTypeE)
  + [`CacheSaltIDType`](#_CPPv4N12tensorrt_llm8executor15CacheSaltIDTypeE)
  + [`LogitsPostProcessor`](#_CPPv4N12tensorrt_llm8executor19LogitsPostProcessorE)
  + [`LogitsPostProcessorMap`](#_CPPv4N12tensorrt_llm8executor22LogitsPostProcessorMapE)
  + [`LogitsPostProcessorBatched`](#_CPPv4N12tensorrt_llm8executor26LogitsPostProcessorBatchedE)
  + [`MedusaChoices`](#_CPPv4N12tensorrt_llm8executor13MedusaChoicesE)
  + [`EagleChoices`](#_CPPv4N12tensorrt_llm8executor12EagleChoicesE)
  + [`PriorityType`](#_CPPv4N12tensorrt_llm8executor12PriorityTypeE)
  + [`BufferView`](#_CPPv4N12tensorrt_llm8executor10BufferViewE)
  + [`DataType`](#_CPPv4N12tensorrt_llm8executor8DataTypeE)
    - [`kBOOL`](#_CPPv4N12tensorrt_llm8executor8DataType5kBOOLE)
    - [`kUINT8`](#_CPPv4N12tensorrt_llm8executor8DataType6kUINT8E)
    - [`kINT8`](#_CPPv4N12tensorrt_llm8executor8DataType5kINT8E)
    - [`kINT32`](#_CPPv4N12tensorrt_llm8executor8DataType6kINT32E)
    - [`kINT64`](#_CPPv4N12tensorrt_llm8executor8DataType6kINT64E)
    - [`kBF16`](#_CPPv4N12tensorrt_llm8executor8DataType5kBF16E)
    - [`kFP8`](#_CPPv4N12tensorrt_llm8executor8DataType4kFP8E)
    - [`kFP16`](#_CPPv4N12tensorrt_llm8executor8DataType5kFP16E)
    - [`kFP32`](#_CPPv4N12tensorrt_llm8executor8DataType5kFP32E)
    - [`kUNKNOWN`](#_CPPv4N12tensorrt_llm8executor8DataType8kUNKNOWNE)
  + [`RequestType`](#_CPPv4N12tensorrt_llm8executor11RequestTypeE)
    - [`REQUEST_TYPE_CONTEXT_AND_GENERATION`](#_CPPv4N12tensorrt_llm8executor11RequestType35REQUEST_TYPE_CONTEXT_AND_GENERATIONE)
    - [`REQUEST_TYPE_CONTEXT_ONLY`](#_CPPv4N12tensorrt_llm8executor11RequestType25REQUEST_TYPE_CONTEXT_ONLYE)
    - [`REQUEST_TYPE_GENERATION_ONLY`](#_CPPv4N12tensorrt_llm8executor11RequestType28REQUEST_TYPE_GENERATION_ONLYE)
  + [`MemoryType`](#_CPPv4N12tensorrt_llm8executor10MemoryTypeE)
    - [`kCPU`](#_CPPv4N12tensorrt_llm8executor10MemoryType4kCPUE)
    - [`kCPU_PINNED`](#_CPPv4N12tensorrt_llm8executor10MemoryType11kCPU_PINNEDE)
    - [`kCPU_PINNEDPOOL`](#_CPPv4N12tensorrt_llm8executor10MemoryType15kCPU_PINNEDPOOLE)
    - [`kGPU`](#_CPPv4N12tensorrt_llm8executor10MemoryType4kGPUE)
    - [`kUVM`](#_CPPv4N12tensorrt_llm8executor10MemoryType4kUVME)
    - [`kUNKNOWN`](#_CPPv4N12tensorrt_llm8executor10MemoryType8kUNKNOWNE)
  + [`ModelType`](#_CPPv4N12tensorrt_llm8executor9ModelTypeE)
    - [`kDECODER_ONLY`](#_CPPv4N12tensorrt_llm8executor9ModelType13kDECODER_ONLYE)
    - [`kENCODER_ONLY`](#_CPPv4N12tensorrt_llm8executor9ModelType13kENCODER_ONLYE)
    - [`kENCODER_DECODER`](#_CPPv4N12tensorrt_llm8executor9ModelType16kENCODER_DECODERE)
  + [`BatchingType`](#_CPPv4N12tensorrt_llm8executor12BatchingTypeE)
    - [`kSTATIC`](#_CPPv4N12tensorrt_llm8executor12BatchingType7kSTATICE)
    - [`kINFLIGHT`](#_CPPv4N12tensorrt_llm8executor12BatchingType9kINFLIGHTE)
  + [`CapacitySchedulerPolicy`](#_CPPv4N12tensorrt_llm8executor23CapacitySchedulerPolicyE)
    - [`kMAX_UTILIZATION`](#_CPPv4N12tensorrt_llm8executor23CapacitySchedulerPolicy16kMAX_UTILIZATIONE)
    - [`kGUARANTEED_NO_EVICT`](#_CPPv4N12tensorrt_llm8executor23CapacitySchedulerPolicy20kGUARANTEED_NO_EVICTE)
    - [`kSTATIC_BATCH`](#_CPPv4N12tensorrt_llm8executor23CapacitySchedulerPolicy13kSTATIC_BATCHE)
  + [`ContextChunkingPolicy`](#_CPPv4N12tensorrt_llm8executor21ContextChunkingPolicyE)
    - [`kFIRST_COME_FIRST_SERVED`](#_CPPv4N12tensorrt_llm8executor21ContextChunkingPolicy24kFIRST_COME_FIRST_SERVEDE)
    - [`kEQUAL_PROGRESS`](#_CPPv4N12tensorrt_llm8executor21ContextChunkingPolicy15kEQUAL_PROGRESSE)
  + [`CommunicationType`](#_CPPv4N12tensorrt_llm8executor17CommunicationTypeE)
    - [`kMPI`](#_CPPv4N12tensorrt_llm8executor17CommunicationType4kMPIE)
  + [`CommunicationMode`](#_CPPv4N12tensorrt_llm8executor17CommunicationModeE)
    - [`kLEADER`](#_CPPv4N12tensorrt_llm8executor17CommunicationMode7kLEADERE)
    - [`kORCHESTRATOR`](#_CPPv4N12tensorrt_llm8executor17CommunicationMode13kORCHESTRATORE)
  + [`RequestStage`](#_CPPv4N12tensorrt_llm8executor12RequestStageE)
    - [`kQUEUED`](#_CPPv4N12tensorrt_llm8executor12RequestStage7kQUEUEDE)
    - [`kENCODER_IN_PROGRESS`](#_CPPv4N12tensorrt_llm8executor12RequestStage20kENCODER_IN_PROGRESSE)
    - [`kCONTEXT_IN_PROGRESS`](#_CPPv4N12tensorrt_llm8executor12RequestStage20kCONTEXT_IN_PROGRESSE)
    - [`kGENERATION_IN_PROGRESS`](#_CPPv4N12tensorrt_llm8executor12RequestStage23kGENERATION_IN_PROGRESSE)
    - [`kGENERATION_COMPLETE`](#_CPPv4N12tensorrt_llm8executor12RequestStage20kGENERATION_COMPLETEE)
  + [`FinishReason`](#_CPPv4N12tensorrt_llm8executor12FinishReasonE)
    - [`kNOT_FINISHED`](#_CPPv4N12tensorrt_llm8executor12FinishReason13kNOT_FINISHEDE)
    - [`kEND_ID`](#_CPPv4N12tensorrt_llm8executor12FinishReason7kEND_IDE)
    - [`kSTOP_WORDS`](#_CPPv4N12tensorrt_llm8executor12FinishReason11kSTOP_WORDSE)
    - [`kLENGTH`](#_CPPv4N12tensorrt_llm8executor12FinishReason7kLENGTHE)
    - [`kTIMED_OUT`](#_CPPv4N12tensorrt_llm8executor12FinishReason10kTIMED_OUTE)
    - [`kCANCELLED`](#_CPPv4N12tensorrt_llm8executor12FinishReason10kCANCELLEDE)
  + [`KvCacheTransferMode`](#_CPPv4N12tensorrt_llm8executor19KvCacheTransferModeE)
    - [`DRAM`](#_CPPv4N12tensorrt_llm8executor19KvCacheTransferMode4DRAME)
    - [`GDS`](#_CPPv4N12tensorrt_llm8executor19KvCacheTransferMode3GDSE)
    - [`POSIX_DEBUG_FALLBACK`](#_CPPv4N12tensorrt_llm8executor19KvCacheTransferMode20POSIX_DEBUG_FALLBACKE)
  + [`operator<<()`](#_CPPv4N12tensorrt_llm8executorlsERNSt7ostreamE23CapacitySchedulerPolicy)
  + [`operator<<()`](#_CPPv4N12tensorrt_llm8executorlsERNSt7ostreamE21ContextChunkingPolicy)
  + [`tensorrt_llm::executor::DebugTensorsPerIteration`](#_CPPv4N12tensorrt_llm8executor24DebugTensorsPerIterationE)
    - [`iter`](#_CPPv4N12tensorrt_llm8executor24DebugTensorsPerIteration4iterE)
    - [`debugTensors`](#_CPPv4N12tensorrt_llm8executor24DebugTensorsPerIteration12debugTensorsE)
  + [`tensorrt_llm::executor::DecodingMode`](#_CPPv4N12tensorrt_llm8executor12DecodingModeE)
    - [`UnderlyingType`](#_CPPv4N12tensorrt_llm8executor12DecodingMode14UnderlyingTypeE)
    - [`useTemperature()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode14useTemperatureEb)
    - [`useOccurrencePenalties()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode22useOccurrencePenaltiesEb)
    - [`usePresencePenalty()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode18usePresencePenaltyEb)
    - [`useRepetitionPenalty()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode20useRepetitionPenaltyEb)
    - [`useFrequencyPenalty()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode19useFrequencyPenaltyEb)
    - [`useMinLength()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode12useMinLengthEb)
    - [`useBanTokens()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode12useBanTokensEb)
    - [`useBanWords()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode11useBanWordsEb)
    - [`useNoRepeatNgramSize()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode20useNoRepeatNgramSizeEb)
    - [`useStopWords()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode12useStopWordsEb)
    - [`useMaxLengthStop()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode16useMaxLengthStopEb)
    - [`useExplicitEosStop()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode18useExplicitEosStopEb)
    - [`useMinP()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode7useMinPEb)
    - [`useVariableBeamWidthSearch()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode26useVariableBeamWidthSearchEb)
    - [`isAuto()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode6isAutoEv)
    - [`isTopK()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode6isTopKEv)
    - [`isTopP()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode6isTopPEv)
    - [`isTopKorTopP()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode12isTopKorTopPEv)
    - [`isTopKandTopP()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode13isTopKandTopPEv)
    - [`isBeamSearch()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode12isBeamSearchEv)
    - [`isMedusa()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode8isMedusaEv)
    - [`isLookahead()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode11isLookaheadEv)
    - [`isExplicitDraftTokens()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode21isExplicitDraftTokensEv)
    - [`isExternalDraftTokens()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode21isExternalDraftTokensEv)
    - [`isEagle()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode7isEagleEv)
    - [`isUseTemperature()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode16isUseTemperatureEv)
    - [`isUsePresencePenalty()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode20isUsePresencePenaltyEv)
    - [`isUseFrequencyPenalty()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode21isUseFrequencyPenaltyEv)
    - [`isUseRepetitionPenalty()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode22isUseRepetitionPenaltyEv)
    - [`isUseMinLength()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode14isUseMinLengthEv)
    - [`isUseOccurrencePenalty()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode22isUseOccurrencePenaltyEv)
    - [`isUsePenalty()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode12isUsePenaltyEv)
    - [`isUseBanWords()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode13isUseBanWordsEv)
    - [`isUseNoRepeatNgramSize()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode22isUseNoRepeatNgramSizeEv)
    - [`isUseBanTokens()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode14isUseBanTokensEv)
    - [`isUseStopWords()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode14isUseStopWordsEv)
    - [`isUseMaxLengthStop()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode18isUseMaxLengthStopEv)
    - [`isUseExplicitEosStop()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode20isUseExplicitEosStopEv)
    - [`isUseStopCriteria()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode17isUseStopCriteriaEv)
    - [`isUseMinP()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode9isUseMinPEv)
    - [`isUseVariableBeamWidthSearch()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode28isUseVariableBeamWidthSearchEv)
    - [`operator==()`](#_CPPv4NK12tensorrt_llm8executor12DecodingModeeqERK12DecodingMode)
    - [`DecodingMode()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode12DecodingModeE14UnderlyingType)
    - [`getState()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode8getStateEv)
    - [`getName()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode7getNameEv)
    - [`Auto()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode4AutoEv)
    - [`TopK()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode4TopKEv)
    - [`TopP()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode4TopPEv)
    - [`TopKTopP()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode8TopKTopPEv)
    - [`BeamSearch()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode10BeamSearchEv)
    - [`Medusa()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode6MedusaEv)
    - [`Lookahead()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode9LookaheadEv)
    - [`ExplicitDraftTokens()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode19ExplicitDraftTokensEv)
    - [`ExternalDraftTokens()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode19ExternalDraftTokensEv)
    - [`Eagle()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode5EagleEv)
    - [`anyBitSet()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode9anyBitSetE14UnderlyingType)
    - [`allBitSet()`](#_CPPv4NK12tensorrt_llm8executor12DecodingMode9allBitSetE14UnderlyingType)
    - [`setBitTo()`](#_CPPv4N12tensorrt_llm8executor12DecodingMode8setBitToE14UnderlyingTypeb)
    - [`mState`](#_CPPv4N12tensorrt_llm8executor12DecodingMode6mStateE)
    - [`kNumFlags`](#_CPPv4N12tensorrt_llm8executor12DecodingMode9kNumFlagsE)
    - [`kUseRepetitionPenalties`](#_CPPv4N12tensorrt_llm8executor12DecodingMode23kUseRepetitionPenaltiesE)
    - [`kUseFrequencyPenalties`](#_CPPv4N12tensorrt_llm8executor12DecodingMode22kUseFrequencyPenaltiesE)
    - [`kUsePresencePenalties`](#_CPPv4N12tensorrt_llm8executor12DecodingMode21kUsePresencePenaltiesE)
    - [`kUseTemperature`](#_CPPv4N12tensorrt_llm8executor12DecodingMode15kUseTemperatureE)
    - [`kUseMinLength`](#_CPPv4N12tensorrt_llm8executor12DecodingMode13kUseMinLengthE)
    - [`kUseBanWords`](#_CPPv4N12tensorrt_llm8executor12DecodingMode12kUseBanWordsE)
    - [`kUseStopWords`](#_CPPv4N12tensorrt_llm8executor12DecodingMode13kUseStopWordsE)
    - [`kUseMaxLengthStop`](#_CPPv4N12tensorrt_llm8executor12DecodingMode17kUseMaxLengthStopE)
    - [`kUseExplicitEosStop`](#_CPPv4N12tensorrt_llm8executor12DecodingMode19kUseExplicitEosStopE)
    - [`kUseNoRepeatNgramSize`](#_CPPv4N12tensorrt_llm8executor12DecodingMode21kUseNoRepeatNgramSizeE)
    - [`kUseMinP`](#_CPPv4N12tensorrt_llm8executor12DecodingMode8kUseMinPE)
    - [`kUseVariableBeamWidthSearch`](#_CPPv4N12tensorrt_llm8executor12DecodingMode27kUseVariableBeamWidthSearchE)
    - [`kUseStandardStopCriteria`](#_CPPv4N12tensorrt_llm8executor12DecodingMode24kUseStandardStopCriteriaE)
    - [`kUseOccurrencePenalties`](#_CPPv4N12tensorrt_llm8executor12DecodingMode23kUseOccurrencePenaltiesE)
    - [`kUsePenalties`](#_CPPv4N12tensorrt_llm8executor12DecodingMode13kUsePenaltiesE)
    - [`kUseBanTokens`](#_CPPv4N12tensorrt_llm8executor12DecodingMode13kUseBanTokensE)
    - [`kAuto`](#_CPPv4N12tensorrt_llm8executor12DecodingMode5kAutoE)
    - [`kTopK`](#_CPPv4N12tensorrt_llm8executor12DecodingMode5kTopKE)
    - [`kTopP`](#_CPPv4N12tensorrt_llm8executor12DecodingMode5kTopPE)
    - [`kBeamSearch`](#_CPPv4N12tensorrt_llm8executor12DecodingMode11kBeamSearchE)
    - [`kMedusa`](#_CPPv4N12tensorrt_llm8executor12DecodingMode7kMedusaE)
    - [`kLookahead`](#_CPPv4N12tensorrt_llm8executor12DecodingMode10kLookaheadE)
    - [`kExplicitDraftTokens`](#_CPPv4N12tensorrt_llm8executor12DecodingMode20kExplicitDraftTokensE)
    - [`kExternalDraftTokens`](#_CPPv4N12tensorrt_llm8executor12DecodingMode20kExternalDraftTokensE)
    - [`kEagle`](#_CPPv4N12tensorrt_llm8executor12DecodingMode6kEagleE)
    - [`kTopKTopP`](#_CPPv4N12tensorrt_llm8executor12DecodingMode9kTopKTopPE)
  + [`tensorrt_llm::executor::DisServingRequestStats`](#_CPPv4N12tensorrt_llm8executor22DisServingRequestStatsE)
    - [`kvCacheTransferMS`](#_CPPv4N12tensorrt_llm8executor22DisServingRequestStats17kvCacheTransferMSE)
    - [`kvCacheSize`](#_CPPv4N12tensorrt_llm8executor22DisServingRequestStats11kvCacheSizeE)
  + [`tensorrt_llm::executor::InflightBatchingStats`](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStatsE)
    - [`numScheduledRequests`](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStats20numScheduledRequestsE)
    - [`numContextRequests`](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStats18numContextRequestsE)
    - [`numGenRequests`](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStats14numGenRequestsE)
    - [`numPausedRequests`](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStats17numPausedRequestsE)
    - [`numCtxTokens`](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStats12numCtxTokensE)
    - [`microBatchId`](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStats12microBatchIdE)
    - [`avgNumDecodedTokensPerIter`](#_CPPv4N12tensorrt_llm8executor21InflightBatchingStats26avgNumDecodedTokensPerIterE)
  + [`tensorrt_llm::executor::IterationStats`](#_CPPv4N12tensorrt_llm8executor14IterationStatsE)
    - [`timestamp`](#_CPPv4N12tensorrt_llm8executor14IterationStats9timestampE)
    - [`iter`](#_CPPv4N12tensorrt_llm8executor14IterationStats4iterE)
    - [`iterLatencyMS`](#_CPPv4N12tensorrt_llm8executor14IterationStats13iterLatencyMSE)
    - [`newActiveRequestsQueueLatencyMS`](#_CPPv4N12tensorrt_llm8executor14IterationStats31newActiveRequestsQueueLatencyMSE)
    - [`numNewActiveRequests`](#_CPPv4N12tensorrt_llm8executor14IterationStats20numNewActiveRequestsE)
    - [`numActiveRequests`](#_CPPv4N12tensorrt_llm8executor14IterationStats17numActiveRequestsE)
    - [`numQueuedRequests`](#_CPPv4N12tensorrt_llm8executor14IterationStats17numQueuedRequestsE)
    - [`numCompletedRequests`](#_CPPv4N12tensorrt_llm8executor14IterationStats20numCompletedRequestsE)
    - [`maxNumActiveRequests`](#_CPPv4N12tensorrt_llm8executor14IterationStats20maxNumActiveRequestsE)
    - [`maxBatchSizeStatic`](#_CPPv4N12tensorrt_llm8executor14IterationStats18maxBatchSizeStaticE)
    - [`maxBatchSizeTunerRecommended`](#_CPPv4N12tensorrt_llm8executor14IterationStats28maxBatchSizeTunerRecommendedE)
    - [`maxBatchSizeRuntime`](#_CPPv4N12tensorrt_llm8executor14IterationStats19maxBatchSizeRuntimeE)
    - [`maxNumTokensStatic`](#_CPPv4N12tensorrt_llm8executor14IterationStats18maxNumTokensStaticE)
    - [`maxNumTokensTunerRecommended`](#_CPPv4N12tensorrt_llm8executor14IterationStats28maxNumTokensTunerRecommendedE)
    - [`maxNumTokensRuntime`](#_CPPv4N12tensorrt_llm8executor14IterationStats19maxNumTokensRuntimeE)
    - [`gpuMemUsage`](#_CPPv4N12tensorrt_llm8executor14IterationStats11gpuMemUsageE)
    - [`cpuMemUsage`](#_CPPv4N12tensorrt_llm8executor14IterationStats11cpuMemUsageE)
    - [`pinnedMemUsage`](#_CPPv4N12tensorrt_llm8executor14IterationStats14pinnedMemUsageE)
    - [`kvCacheStats`](#_CPPv4N12tensorrt_llm8executor14IterationStats12kvCacheStatsE)
    - [`crossKvCacheStats`](#_CPPv4N12tensorrt_llm8executor14IterationStats17crossKvCacheStatsE)
    - [`staticBatchingStats`](#_CPPv4N12tensorrt_llm8executor14IterationStats19staticBatchingStatsE)
    - [`inflightBatchingStats`](#_CPPv4N12tensorrt_llm8executor14IterationStats21inflightBatchingStatsE)
    - [`specDecodingStats`](#_CPPv4N12tensorrt_llm8executor14IterationStats17specDecodingStatsE)
  + [`tensorrt_llm::executor::KvCacheStats`](#_CPPv4N12tensorrt_llm8executor12KvCacheStatsE)
    - [`maxNumBlocks`](#_CPPv4N12tensorrt_llm8executor12KvCacheStats12maxNumBlocksE)
    - [`freeNumBlocks`](#_CPPv4N12tensorrt_llm8executor12KvCacheStats13freeNumBlocksE)
    - [`usedNumBlocks`](#_CPPv4N12tensorrt_llm8executor12KvCacheStats13usedNumBlocksE)
    - [`tokensPerBlock`](#_CPPv4N12tensorrt_llm8executor12KvCacheStats14tokensPerBlockE)
    - [`allocTotalBlocks`](#_CPPv4N12tensorrt_llm8executor12KvCacheStats16allocTotalBlocksE)
    - [`allocNewBlocks`](#_CPPv4N12tensorrt_llm8executor12KvCacheStats14allocNewBlocksE)
    - [`reusedBlocks`](#_CPPv4N12tensorrt_llm8executor12KvCacheStats12reusedBlocksE)
    - [`missedBlocks`](#_CPPv4N12tensorrt_llm8executor12KvCacheStats12missedBlocksE)
    - [`cacheHitRate`](#_CPPv4N12tensorrt_llm8executor12KvCacheStats12cacheHitRateE)
  + [`tensorrt_llm::executor::RequestPerfMetrics`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetricsE)
    - [`TimePoint`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics9TimePointE)
    - [`timingMetrics`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13timingMetricsE)
    - [`kvCacheMetrics`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics14kvCacheMetricsE)
    - [`speculativeDecoding`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics19speculativeDecodingE)
    - [`firstIter`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics9firstIterE)
    - [`lastIter`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics8lastIterE)
    - [`iter`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics4iterE)
    - [`tensorrt_llm::executor::RequestPerfMetrics::KvCacheMetrics`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics14KvCacheMetricsE)
      * [`numTotalAllocatedBlocks`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics14KvCacheMetrics23numTotalAllocatedBlocksE)
      * [`numNewAllocatedBlocks`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics14KvCacheMetrics21numNewAllocatedBlocksE)
      * [`numReusedBlocks`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics14KvCacheMetrics15numReusedBlocksE)
      * [`numMissedBlocks`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics14KvCacheMetrics15numMissedBlocksE)
      * [`kvCacheHitRate`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics14KvCacheMetrics14kvCacheHitRateE)
    - [`tensorrt_llm::executor::RequestPerfMetrics::SpeculativeDecodingMetrics`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics26SpeculativeDecodingMetricsE)
      * [`acceptanceRate`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics26SpeculativeDecodingMetrics14acceptanceRateE)
      * [`totalAcceptedDraftTokens`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics26SpeculativeDecodingMetrics24totalAcceptedDraftTokensE)
      * [`totalDraftTokens`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics26SpeculativeDecodingMetrics16totalDraftTokensE)
    - [`tensorrt_llm::executor::RequestPerfMetrics::TimingMetrics`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13TimingMetricsE)
      * [`arrivalTime`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13TimingMetrics11arrivalTimeE)
      * [`firstScheduledTime`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13TimingMetrics18firstScheduledTimeE)
      * [`firstTokenTime`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13TimingMetrics14firstTokenTimeE)
      * [`lastTokenTime`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13TimingMetrics13lastTokenTimeE)
      * [`kvCacheTransferStart`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13TimingMetrics20kvCacheTransferStartE)
      * [`kvCacheTransferEnd`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13TimingMetrics18kvCacheTransferEndE)
      * [`kvCacheSize`](#_CPPv4N12tensorrt_llm8executor18RequestPerfMetrics13TimingMetrics11kvCacheSizeE)
  + [`tensorrt_llm::executor::RequestStats`](#_CPPv4N12tensorrt_llm8executor12RequestStatsE)
    - [`id`](#_CPPv4N12tensorrt_llm8executor12RequestStats2idE)
    - [`stage`](#_CPPv4N12tensorrt_llm8executor12RequestStats5stageE)
    - [`contextPrefillPosition`](#_CPPv4N12tensorrt_llm8executor12RequestStats22contextPrefillPositionE)
    - [`numGeneratedTokens`](#_CPPv4N12tensorrt_llm8executor12RequestStats18numGeneratedTokensE)
    - [`avgNumDecodedTokensPerIter`](#_CPPv4N12tensorrt_llm8executor12RequestStats26avgNumDecodedTokensPerIterE)
    - [`scheduled`](#_CPPv4N12tensorrt_llm8executor12RequestStats9scheduledE)
    - [`paused`](#_CPPv4N12tensorrt_llm8executor12RequestStats6pausedE)
    - [`disServingStats`](#_CPPv4N12tensorrt_llm8executor12RequestStats15disServingStatsE)
    - [`allocTotalBlocksPerRequest`](#_CPPv4N12tensorrt_llm8executor12RequestStats26allocTotalBlocksPerRequestE)
    - [`allocNewBlocksPerRequest`](#_CPPv4N12tensorrt_llm8executor12RequestStats24allocNewBlocksPerRequestE)
    - [`reusedBlocksPerRequest`](#_CPPv4N12tensorrt_llm8executor12RequestStats22reusedBlocksPerRequestE)
    - [`missedBlocksPerRequest`](#_CPPv4N12tensorrt_llm8executor12RequestStats22missedBlocksPerRequestE)
    - [`kvCacheHitRatePerRequest`](#_CPPv4N12tensorrt_llm8executor12RequestStats24kvCacheHitRatePerRequestE)
  + [`tensorrt_llm::executor::RequestStatsPerIteration`](#_CPPv4N12tensorrt_llm8executor24RequestStatsPerIterationE)
    - [`iter`](#_CPPv4N12tensorrt_llm8executor24RequestStatsPerIteration4iterE)
    - [`requestStats`](#_CPPv4N12tensorrt_llm8executor24RequestStatsPerIteration12requestStatsE)
  + [`tensorrt_llm::executor::SpecDecodingStats`](#_CPPv4N12tensorrt_llm8executor17SpecDecodingStatsE)
    - [`numDraftTokens`](#_CPPv4N12tensorrt_llm8executor17SpecDecodingStats14numDraftTokensE)
    - [`numAcceptedTokens`](#_CPPv4N12tensorrt_llm8executor17SpecDecodingStats17numAcceptedTokensE)
    - [`numRequestsWithDraftTokens`](#_CPPv4N12tensorrt_llm8executor17SpecDecodingStats26numRequestsWithDraftTokensE)
    - [`acceptanceLength`](#_CPPv4N12tensorrt_llm8executor17SpecDecodingStats16acceptanceLengthE)
    - [`iterLatencyMS`](#_CPPv4N12tensorrt_llm8executor17SpecDecodingStats13iterLatencyMSE)
    - [`draftOverhead`](#_CPPv4N12tensorrt_llm8executor17SpecDecodingStats13draftOverheadE)
  + [`tensorrt_llm::executor::StaticBatchingStats`](#_CPPv4N12tensorrt_llm8executor19StaticBatchingStatsE)
    - [`numScheduledRequests`](#_CPPv4N12tensorrt_llm8executor19StaticBatchingStats20numScheduledRequestsE)
    - [`numContextRequests`](#_CPPv4N12tensorrt_llm8executor19StaticBatchingStats18numContextRequestsE)
    - [`numCtxTokens`](#_CPPv4N12tensorrt_llm8executor19StaticBatchingStats12numCtxTokensE)
    - [`numGenTokens`](#_CPPv4N12tensorrt_llm8executor19StaticBatchingStats12numGenTokensE)
    - [`emptyGenSlots`](#_CPPv4N12tensorrt_llm8executor19StaticBatchingStats13emptyGenSlotsE)
  + [`tensorrt_llm::executor::TypeTraits`](#_CPPv4I0_bEN12tensorrt_llm8executor10TypeTraitsE)
  + [`tensorrt_llm::executor::TypeTraits< bool >`](#_CPPv4IEN12tensorrt_llm8executor10TypeTraitsIbEE)
    - [`value`](#_CPPv4N12tensorrt_llm8executor10TypeTraitsIbE5valueE)
  + [`tensorrt_llm::executor::TypeTraits< float >`](#_CPPv4IEN12tensorrt_llm8executor10TypeTraitsIfEE)
    - [`value`](#_CPPv4N12tensorrt_llm8executor10TypeTraitsIfE5valueE)
  + [`tensorrt_llm::executor::TypeTraits< half >`](#_CPPv4IEN12tensorrt_llm8executor10TypeTraitsI4halfEE)
    - [`value`](#_CPPv4N12tensorrt_llm8executor10TypeTraitsI4halfE5valueE)
  + [`tensorrt_llm::executor::TypeTraits< std::int32_t >`](#_CPPv4IEN12tensorrt_llm8executor10TypeTraitsINSt7int32_tEEE)
    - [`value`](#_CPPv4N12tensorrt_llm8executor10TypeTraitsINSt7int32_tEE5valueE)
  + [`tensorrt_llm::executor::TypeTraits< std::int64_t >`](#_CPPv4IEN12tensorrt_llm8executor10TypeTraitsINSt7int64_tEEE)
    - [`value`](#_CPPv4N12tensorrt_llm8executor10TypeTraitsINSt7int64_tEE5valueE)
  + [`tensorrt_llm::executor::TypeTraits< std::int8_t >`](#_CPPv4IEN12tensorrt_llm8executor10TypeTraitsINSt6int8_tEEE)
    - [`value`](#_CPPv4N12tensorrt_llm8executor10TypeTraitsINSt6int8_tEE5valueE)
  + [`tensorrt_llm::executor::TypeTraits< std::uint8_t >`](#_CPPv4IEN12tensorrt_llm8executor10TypeTraitsINSt7uint8_tEEE)
    - [`value`](#_CPPv4N12tensorrt_llm8executor10TypeTraitsINSt7uint8_tEE5valueE)
  + [`tensorrt_llm::executor::TypeTraits< T * >`](#_CPPv4I0EN12tensorrt_llm8executor10TypeTraitsIP1TEE)
    - [`value`](#_CPPv4N12tensorrt_llm8executor10TypeTraitsIP1TE5valueE)