class PCMProcessor extends AudioWorkletProcessor {
    process(inputs, outputs, parameters) {
        const input = inputs[0];
        if (input.length > 0) {
            const inputData = input[0];
            // Kirim data audio mentah (Float32Array) ke thread utama
            this.port.postMessage(inputData);
        }
        return true;
    }
}

registerProcessor('pcm-processor', PCMProcessor);
