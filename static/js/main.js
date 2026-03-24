document.addEventListener('DOMContentLoaded', function() {
    const uploadArea = document.getElementById('uploadArea');
    const fileInput = document.getElementById('file');
    const previewContainer = document.getElementById('previewContainer');
    const previewImage = document.getElementById('previewImage');
    const previewInfo = document.getElementById('previewInfo');
    const removeBtn = document.getElementById('removeFile');
    const uploadForm = document.getElementById('uploadForm');
    const loadingOverlay = document.getElementById('loadingOverlay');
    
    let selectedFile = null;
    
    if (uploadArea && fileInput) {
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            uploadArea.addEventListener(eventName, preventDefaults, false);
        });
        
        function preventDefaults(e) {
            e.preventDefault();
            e.stopPropagation();
        }
        
        ['dragenter', 'dragover'].forEach(eventName => {
            uploadArea.addEventListener(eventName, () => {
                uploadArea.classList.add('dragover');
            }, false);
        });
        
        ['dragleave', 'drop'].forEach(eventName => {
            uploadArea.addEventListener(eventName, () => {
                uploadArea.classList.remove('dragover');
            }, false);
        });
        
        uploadArea.addEventListener('drop', handleDrop, false);
        uploadArea.addEventListener('change', handleFileSelect, false);
        
        removeBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            removeFile();
        });
    }
    
    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        if (files.length > 0) {
            handleFiles(files[0]);
        }
    }
    
    function handleFileSelect(e) {
        const files = e.target.files;
        if (files.length > 0) {
            handleFiles(files[0]);
        }
    }
    
    function handleFiles(file) {
        const validTypes = ['image/jpeg', 'image/jpg'];
        
        if (!validTypes.includes(file.type.toLowerCase())) {
            showError('Please select a JPG or JPEG image file.');
            return;
        }
        
        selectedFile = file;
        
        const reader = new FileReader();
        reader.onload = function(e) {
            previewImage.src = e.target.result;
            uploadArea.classList.add('has-file');
            previewContainer.classList.add('visible');
            
            const sizeKB = (file.size / 1024).toFixed(1);
            const sizeMB = (file.size / (1024 * 1024)).toFixed(2);
            const sizeText = sizeMB > 1 ? `${sizeMB} MB` : `${sizeKB} KB`;
            
            previewInfo.innerHTML = `<strong>${file.name}</strong><br>Size: ${sizeText}`;
            
            const title = uploadArea.querySelector('.upload-area__title');
            const subtitle = uploadArea.querySelector('.upload-area__subtitle');
            if (title) title.textContent = 'Image Selected';
            if (subtitle) subtitle.textContent = file.name;
        };
        reader.readAsDataURL(file);
    }
    
    function removeFile() {
        selectedFile = null;
        fileInput.value = '';
        previewImage.src = '';
        uploadArea.classList.remove('has-file');
        previewContainer.classList.remove('visible');
        
        const title = uploadArea.querySelector('.upload-area__title');
        const subtitle = uploadArea.querySelector('.upload-area__subtitle');
        if (title) title.textContent = 'Drag & Drop your image here';
        if (subtitle) subtitle.textContent = 'or click to browse files';
    }
    
    function showError(message) {
        const existingAlert = document.querySelector('.alert--error');
        if (existingAlert) existingAlert.remove();
        
        const alertHtml = `
            <div class="alert alert--error">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" y1="8" x2="12" y2="12"></line>
                    <line x1="12" y1="16" x2="12.01" y2="16"></line>
                </svg>
                <span>${message}</span>
            </div>
        `;
        
        const form = document.getElementById('uploadForm');
        if (form) form.insertAdjacentHTML('beforebegin', alertHtml);
    }
    
    if (uploadForm) {
        uploadForm.addEventListener('submit', function() {
            showLoading();
        });
    }
    
    function showLoading() {
        if (loadingOverlay) {
            loadingOverlay.classList.add('visible');
        }
    }
    
    window.continueWithSignature = function() {
        const typeSelect = document.getElementById('img_type');
        if (typeSelect) {
            typeSelect.value = 'Signature';
            document.querySelector('.card').scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    };
    
    window.scrollToForm = function() {
        document.querySelector('.card').scrollIntoView({ behavior: 'smooth', block: 'center' });
    };
});
