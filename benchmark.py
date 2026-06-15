import time
import json
import whisper
import jiwer

# 1. Define model tiers 
models_to_test = ["tiny", "base", "small"]

# 2. Updated Data Matrix 
audio_files = {
    "1_clean_baseline": {
        "path": "audio_samples/clean_baseline.mp3",
        "ground_truth": "I am a backend developer. I design scalable API microservices using the FastAPI framework and Python."
    },
    "2_background_noise": {
        "path": "audio_samples/background_noise.mp3",
        "ground_truth": "In my previous workspace, I configured PostgreSQL databases inside Docker container volumes for data persistence."
    },
    "3_regional_accent": {
        "path": "audio_samples/regional_accent.mp3",
        "ground_truth": "We need to optimize the network throughput by managing intermediate web proxy and disabling buffering lines."
    },
    "4_technical_jargon": {
        "path": "audio_samples/custom_tech_jargon.mp3",
        "ground_truth": "Our automated monitoring pipeline relies on YOLO v8 for deep learning object detection, MediaPipe for face landmarks and the FastAPI backend."
    },
    "5_speed_mumble": {
        "path": "audio_samples/speed_mumble.mp3",
        "ground_truth": "When a client suddenly terminates their browser tab session, a signal clears the server task memory instantly."
    },
    "6_long_payload": {
        "path": "audio_samples/long_recording.mp3",
        "ground_truth": "The primary objective of this architecture is to provide an automated, fair, and reliable interview environment by combining multiple machine learning models. Instead of looking at a single rule, our platform processes continuous video streams, audio data, and contextual language outputs simultaneously. The video system extracts features like multi-person detection and mobile phone usage using convolutional neural networks, while the acoustic engine evaluates ambient sound cues. This multi-modal strategy ensures maximum security against candidate cheating and minimizes false alert warnings drastically."
    },
    "7_small_payload":{
        "path": "audio_samples/small_recording.mp3",
        "ground_truth": "I have worked with Python and FastAPI."
    }
    
}

print("🚀 STARTING WHISPER PERFORMANCE BENCHMARKING ENGINE")
print("="*70)

# 3. Execution Benchmarking Pipeline Loop
for model_name in models_to_test:
    print(f"\n⚙️ LOADING MODEL TIER: [{model_name.upper()}]...")
    model = whisper.load_model(model_name)
    
    for key, data in audio_files.items():
        # Trigger high-precision clock
        start_time = time.perf_counter()
        
        # Execute Speech-to-Text inference
        result = model.transcribe(data["path"])
        
        # Terminate clock to compute processing overhead
        end_time = time.perf_counter()
        processing_time = round(end_time - start_time, 2)
        
        # Calculate linguistic discrepancy (Word Error Rate)
        wer = jiwer.wer(data["ground_truth"], result["text"])
        
        # Standardized Target Output Payload mapping
        output_json = {
            "transcript": result["text"].strip(),
            "processing_time": processing_time
        }
        
        print(f" 📂 Test Scenario: {key}")
        print(f"    ⏱️ Processing Time: {processing_time}s")
        print(f"    📉 Word Error Rate: {wer:.2%}")
        print(json.dumps(output_json, indent=4))
        print("-" * 50)

print("\n🏆 Benchmarking Execution Complete. Log details captured.")